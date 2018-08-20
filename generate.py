import asyncio

from aiodns import DNSResolver

loop = asyncio.get_event_loop()
resolver = DNSResolver(loop=loop)

def get_entries(file):
    with open(file, "r") as entries:
        return entries.readlines()

def remove_duplicates(file):
    """
    Remove duplicate entries from a file.
    """

    entries = get_entries(file)
    with open(file, "w") as new:
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
                ip_blacklist.writelines(["{}\n".format(ip.host) for ip in ips])
            except Exception:
                print("Failed to resolve domain {}.".format(entry.strip()))

def generate_cloaking_rules(entries):
    with open("cloaking-rules", "w") as cloaking:
        cloaking.writelines(["{} 0.0.0.0\n".format(entry.strip()) for entry in entries])

async def main():
    print("Sorting blacklist.")
    sort_blacklist(get_entries("blacklist"))

    print("Generating IP blacklist.")
    await generate_ip_blacklist(get_entries("blacklist"))

    print("Generating cloaking rules.")
    generate_cloaking_rules(get_entries("blacklist"))

    print("Removing duplicates from blacklist.")
    remove_duplicates("blacklist")

    print("Removing duplicates from IP blacklist.")
    remove_duplicates("ip-blacklist")

    print("Removing duplicates from cloaking rules.")
    remove_duplicates("cloaking-rules")

loop.run_until_complete(main())