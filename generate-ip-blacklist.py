import asyncio

from aiodns import DNSResolver

async def generate_ip_blacklist(resolver):
	hosts = open("blacklist", "r")
	ip_blacklist = open("ip-blacklist", "w+")

	for entry in hosts.readlines():
		# Skip whitespace.
		if entry.isspace():
			ip_blacklist.write("\n")
			continue

		# Write comments.
		if "#" in entry:
			ip_blacklist.write(entry)
			continue
		
		try:
			# Resolve domain.
			ips = await resolver.query(entry.strip(), "A")

			for ip in ips:
				# Write IP blacklist rule.
				ip_blacklist.write("{}\n".format(ip.host))
		except Exception:
			print("Failed to resolve domain {}.".format(entry.strip()))

	ip_blacklist.close()

loop = asyncio.get_event_loop()

resolver = DNSResolver(loop=loop)
loop.run_until_complete(generate_ip_blacklist(resolver))