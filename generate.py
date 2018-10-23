import asyncio

from aiodns import DNSResolver
from aiodns.error import DNSError

loop = asyncio.get_event_loop()
resolver = DNSResolver(loop=loop)

def get_entries(file):
    with open(file, "r") as entries:
        return entries.readlines()

def sort_entries(file):
    """
    Sort the blacklist alphabetically. Keeps things nice and ordered.
    """

    entries = get_entries(file)
    entries.sort()

    with open(file, "w") as new:
        new.writelines(["{}".format(entry) for entry in entries])

async def remove_dead_entries(entries):
    """
    Remove any domains which don't have A (IPv4) or AAAA (IPv6) records.
    Could be written better...
    """
    alive = []

    for entry in set(entries):
        ipv4 = True
        ipv6 = True

        try:
            ips = await resolver.query(entry.strip(), "A")
        except DNSError:
            ipv4 = False

        try:
            ips = await resolver.query(entry.strip(), "AAAA")
        except DNSError:
            ipv6 = False

        if ipv4 or ipv6:
            alive.append(entry)

    return alive

def remove_duplicates(file):
    """
    Remove duplicate entries from a file.
    """

    entries = get_entries(file)
    
    with open(file, "w") as new:
        for entry in set(entries):
            new.write(entry)

async def generate_ip_blacklist(entries):
    with open("ip-blacklist", "w") as ip_blacklist:
        for entry in entries:
            try:
                ips = await resolver.query(entry.strip(), "A")
                ip_blacklist.writelines(["{}\n".format(ip.host) for ip in ips])
            except Exception:
                pass

            try:
                ips = await resolver.query(entry.strip(), "AAAA")
                ip_blacklist.writelines(["{}\n".format(ip.host) for ip in ips])
            except Exception:
                pass

def generate_cloaking_rules(entries):
    with open("cloaking-rules", "w") as cloaking:
        cloaking.writelines(["{} 0.0.0.0\n".format(entry.strip()) for entry in entries])

async def main():
    entries = await remove_dead_entries(get_entries("blacklist"))

    with open("blacklist", "w") as blacklist:
        blacklist.writelines([entry for entry in entries])

    print("Generating IP blacklist.")
    await generate_ip_blacklist(entries)

    print("Generating cloaking rules.")
    generate_cloaking_rules(entries)

    print("Removing duplicates from blacklist.")
    remove_duplicates("blacklist")

    print("Removing duplicates from IP blacklist.")
    remove_duplicates("ip-blacklist")

    print("Removing duplicates from cloaking rules.")
    remove_duplicates("cloaking-rules")

    print("Sorting blacklist.")
    sort_entries("blacklist")

    print("Sorting IP blacklist.")
    sort_entries("ip-blacklist")

    print("Sorting cloaking rules.")
    sort_entries("cloaking-rules")
    

loop.run_until_complete(main())