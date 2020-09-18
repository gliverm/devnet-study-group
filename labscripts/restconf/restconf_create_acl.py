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

# Ensure that the Content-Type and Accept header fields are set
headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}

data = {
  "openconfig-acl:acl-set": [
    {
      "name": "TEST",
      "type": "openconfig-acl:ACL_IPV4",
      "config": {
        "name": "TEST",
        "type": "openconfig-acl:ACL_IPV4"
      },
      "acl-entries": {
        "acl-entry": [
          {
            "sequence-id": 10,
            "config": {
              "sequence-id": 10
            },
            "ipv4": {
              "config": {
                "source-address": "10.10.10.0/24",
                "destination-address": "20.20.20.1/24",
                "protocol": "openconfig-packet-match-types:IP_TCP"
              }
            },
            "transport": {
              "config": {
                "source-port": "ANY",
                "destination-port": "ANY"
              }
            },
            "actions": {
              "config": {
                "forwarding-action": "openconfig-acl:ACCEPT",
                "log-action": "openconfig-acl:LOG_NONE"
              }
            }
          }
        ]
      }
    }
  ]
}

def create():
    acl = "TEST"
    payload = json.dumps(data)
    url = f"https://{hostname}/restconf/data/openconfig-acl:acl/acl-sets/"
    response = requests.post(url, 
                             auth=(user, password), 
                             headers=headers, 
                             data=payload, 
                             verify=False
    )

    if response.ok:
        print(f'Successfully Created {acl}')
    else:
        print(f'Could not create ACL \n{acl}')

if __name__ == '__main__':
    create()