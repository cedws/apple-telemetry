import asyncio

from aiodns import DNSResolver

loop = asyncio.get_event_loop()
resolver = DNSResolver(loop=loop)

def get_entries():
    with open("blacklist", "r") as blacklist:
        return blacklist.readlines()

def remove_duplicates_from_blacklist(entries):
    """
    Remove duplicate entries from the blacklist.
    """
    
    with open("blacklist", "w") as new:
        for entry in set(entries):
            new.write(entry)

def sort_blacklist(entries):
    """
    Sort the blacklist alphabetically. Keeps things nice and ordered.
    """

    with open("blacklist", "w") as new:
        entries.sort()
        new.writelines(["{}".format(entry) for entry in entries])

async def generate_ip_blacklist(entries):
    with open("ip-blacklist", "w") as ip_blacklist:
        for entry in entries:
            try:
                ips = await resolver.query(entry.strip(), "A")
            except Exception:
                print("Failed to resolve domain {}.".format(entry.strip()))

            ip_blacklist.writelines(["{}\n".format(ip.host) for ip in ips])

def generate_cloaking_rules(entries):
    with open("cloaking-rules", "w") as cloaking:
        cloaking.writelines(["{} 0.0.0.0\n".format(entry.strip()) for entry in entries])

async def main():
    print("Removing duplicates from blacklist.")
    remove_duplicates_from_blacklist(get_entries())

    print("Sorting blacklist.")
    sort_blacklist(get_entries())

    print("Generating IP blacklist.")
    await generate_ip_blacklist(get_entries())

    print("Generating cloaking rules.")
    generate_cloaking_rules(get_entries())

loop.run_until_complete(main())