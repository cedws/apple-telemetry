#!/usr/bin/env python3

import sys
import datetime
import json

def main():
    rules = []
    for entry in sys.stdin:
        rules.append({
            "action": "deny",
            "direction": "outgoing",
            "priority": "regular",
            "process": "any",
            "remote-domains": entry.strip()
        })

    desc = "Source: https://github.com/adversarialtools/apple-telemetry | Domains: {} | Updated: {}".format(len(rules), datetime.datetime.now())
    root = {
        "description": desc,
        "name": "apple_telemetry",
        "rules": rules
    }

    print(json.dumps(root))

if __name__ == "__main__":
    main()
