# `ios-telemetry`
Domain blocklists, IP blocklists, and cloaking files for domains that iOS frequently contacts (not all of them are telemetry!). DNSCloak is an excellent app capable of using these files, but it's a bit of a pain to get the blocklists onto your device. 

# Contribution
If you come across any other domains, please submit a PR! Add the entries to the `blacklist` file with a comment if applicable, then run `generate_cloaking_rules.py` and `generate_ip_blacklist.py` with Python 3.

# Notes
**Warning:** This is not an exhaustive list. There are hundreds of domains contacted on a regular basis by iOS, with no consistent naming scheme or obvious purpose. If you want to block all domains, you should use a whitelist.

**Warning:** Some domains may not be related to Apple. I've had to filter out the domains from my own blacklist log manually. However, some domains such as `weather.com` are contacted by built-in applications (Weather). Entries like these belong in this repository.

**Warning:** Services such as updates, App Store, and Apple Pay will probably be blocked. It is up to you to remove the domains you don't wish to block.