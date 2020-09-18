#!/usr/bin/env python

import json
import requests 

hostname = 'r1.lab.local'
user = 'wwt'
password = 'WWTwwt1!'

# Suppress SSL certificate verification errors
# Using self-signed certificates in lab and therefore will otherwise report verbos
#   SSL validation errors
requests.packages.urllib3.disable_warnings()

restconf_url = f"https://{hostname}/restconf/data/"
module_uri = "ietf-interfaces:interfaces"

# Ensure that the Content-Type and Accept header fields are set
headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}

data = {
    "ietf-interfaces:interface": {
        "name": "Loopback1",
        "description": "New Loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": "true",
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "1.1.1.1",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}

def create():
    # Build the full URL for the request
    interface = "Loopback1"
    full_url = f"{restconf_url}{module_uri}"

    # Convert data dictionary to a string to be used in request
    payload = json.dumps(data)
    response = requests.post(
        full_url, auth=(user, password), headers=headers, data=payload, verify=False
    )

    if response.ok:
        print(f'Successfully Created {interface}')
    else:
        print(f'Could not create Interface \n{response}')

if __name__ == '__main__':
    create()