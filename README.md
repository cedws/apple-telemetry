# `ios-telemetry`

Domain blocklists, IP blocklists, and cloaking files for domains that iOS frequently contacts. DNSCloak is an excellent app capable of using these files, but it's a bit of a pain to get the blocklists onto your device. **Services such as updates, App Store, and Apple Pay will probably be blocked by this list.** You can remove entries manually, but this is tedious, so I recommend just temporarily disabling the blocklist when necessary.

# Why?

Users should have more control over the telemetry sent by their smartphones. Not only that, but I've seen a large improvement to my device's battery life while using these blocklists.

# Usage

- Download DNSCloak, or another app capable of using DNS blocklists
- Navigate to this repository in Safari
- Copy the desired blocklist to your clipboard (`cloaking-rules` is recommended)
- Download Textor, or another app capable of saving text to Files
- In Textor, create a new file and paste the blocklist
- Remove domains for services you wish to use (such as Apple Pay)
- Navigate to the DNSCloak settings and select the saved blocklist

# Links

- [Purpose of each domain](https://github.com/c-edw/ios-telemetry/wiki/Domains)
- https://stan.sh/posts/dns-requests-of-ios-devices
- https://cedwards.xyz/blog/ios-dns-privacy-investigation/

# Notes

* This is not an exhaustive list. There are hundreds of domains contacted on a regular basis by iOS, with no consistent naming scheme or obvious purpose. If you want to block all domains, you should use a whitelist.

* Some domains may not be related to Apple. I've had to filter out the domains from my own blacklist log manually. However, some domains such as `weather.com` are contacted by built-in applications (Weather). Entries like these belong in this repository.

# Contribution

If you come across any other domains, please submit a PR! Add the entries to the `blacklist` file then run `generate.py` with Python 3. It can take a few minutes because it has to make a lot of DNS queries.