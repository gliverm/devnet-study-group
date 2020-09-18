#!/usr/bin/env python

import json
import requests
from pprint import pprint 

hostname = 'r1.lab.local'
user = 'wwt'
password = 'WWTwwt1!'

# Suppress SSL certificate verification errors
# Using self-signed certificates in lab and therefore will otherwise report verbos
#   SSL validation errors
requests.packages.urllib3.disable_warnings()

restconf_url = f"https://{hostname}/restconf/data/"
module_uri = "native"

# Ensure that the Content-Type and Accept header fields are set
headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}

def retrieve():
    full_url = restconf_url + module_uri
    # Full URL includes: the host, port, and module path
    # Login auth details
    # Headers
    # Verify set to False to instruct requests not to vlaidate SSL certificate
    response = requests.get(
        full_url, auth=(user, password), headers=headers, verify=False
    )

    if response.ok:
        # print the JSON encoded configurationdetails
        print(response.json())
        # pprint(response.json())  # Not all that pretty because bigger than screen
    else:
        print('Could not retrieve configuration')

if __name__ == '__main__':
    retrieve()