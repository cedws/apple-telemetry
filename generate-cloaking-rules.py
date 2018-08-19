UNREACHABLE = "0.0.0.0"

def generate_cloaking_rules(unreachable):
	hosts = open("blacklist", "r")
	cloaking = open("cloaking", "w+")

	for entry in hosts.readlines():
		# Skip whitespace.
		if entry.isspace():
			cloaking.write("\n")
			continue

		# Write comments.
		if "#" in entry:
			cloaking.write(entry)
			continue
 		
 		# Write cloaking rule.
		cloaking.write("{}\t{}".format(entry, unreachable))

	cloaking.close()

generate_cloaking_rules(UNREACHABLE)