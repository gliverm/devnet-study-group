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
module_uri = 'ietf-interfaces:interfaces/interface'

# Ensure that the Content-Type and Accept header fields are set
headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}

def delete():
    # Build the full URL for the request
    interface = "Loopback1"
    full_url = f"{restconf_url}{module_uri}={interface}"

    # Delete Interface
    response = requests.delete(full_url, 
                            auth=(user, password), 
                            headers=headers, 
                            verify=False
    )

    if response.ok:
        print(f'Successfully Deleted {interface}')
    else:
        print(f'Could not delete Interface \n{response.text}')

if __name__ == '__main__':
    delete()