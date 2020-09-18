#!/usr/bin/env python

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

def save():
    full_url = f"https://{hostname}/restconf/operations/cisco-ia:save-config/"
    # RPC Call to Save IOS
    response = requests.post(full_url, 
                            auth=(user, password), 
                            headers=headers, 
                            verify=False
    )

    if response.ok:
        print('Configuration saved successfully')
    else:
        print('Could not save configuration')

if __name__ == '__main__':
    save()