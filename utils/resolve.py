#!/usr/bin/env python3

import asyncio
import sys

from aiodns import DNSResolver
from aiodns.error import DNSError

loop = asyncio.get_event_loop()
resolver = DNSResolver(loop=loop, nameservers=["1.1.1.1", "8.8.8.8"])

async def main():
    for entry in sys.stdin:
        try:
            ips = await resolver.query(entry.strip(), "A")
            for ip in ips:
                print(ip.host)
        except Exception:
            pass

        try:
            ips = await resolver.query(entry.strip(), "AAAA")
            for ip in ips:
                print(ip.host)
        except Exception:
            pass

loop.run_until_complete(main())
