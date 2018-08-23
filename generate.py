import asyncio

from aiodns import DNSResolver

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
                print("Failed to resolve domain {}.".format(entry.strip()))

def generate_cloaking_rules(entries):
    with open("cloaking-rules", "w") as cloaking:
        cloaking.writelines(["{} 0.0.0.0\n".format(entry.strip()) for entry in entries])

async def main():
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

    print("Sorting blacklist.")
    sort_entries("blacklist")

    print("Sorting IP blacklist.")
    sort_entries("ip-blacklist")

    print("Sorting cloaking rules.")
    sort_entries("cloaking-rules")
    

loop.run_until_complete(main())