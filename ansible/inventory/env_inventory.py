#!/usr/bin/env python3
# Inventory
import json

host_ip = "192.168.0.213"

inventory = {
    "_meta": {
        "hostvars": {
            host_ip: {
                "ansible_user": "j",
                "ansible_python_interpreter": "/usr/bin/python3"
            }
        }
    },
    "all": {
        "hosts": [host_ip]
    }
}

print(json.dumps(inventory))
