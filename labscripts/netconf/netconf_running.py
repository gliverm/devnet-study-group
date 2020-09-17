#!/usr/bin/env python

import xmltodict
import yaml
from ncclient import manager

def main():
    
    with open('device.yml', 'r') as fp:
        device = yaml.safe_load(fp.read())

    with manager.connect(**device, hostkey_verify=False) as mgr:

        # Retrieve the configuration from the 'running' 
        #   datastore using a get-config operation
        resp = mgr.get_config('running').xml

        # Load the XML response as a Python dictionary
        resp_dict = xmltodict.parse(resp)

        # Extract the 'data' from the rpc-reply
        running_config = resp_dict['rpc-reply']['data']

        # Save the running config locally
        hostname = running_config['native']['hostname']
        with open(hostname + '.running-config.xml', 'w') as fp:
            fp.write(resp)

        # Display HTTP and HTTPS server statuses from the configuration
        ip_settings = running_config['native']['ip']
        print(f"hostname:  {hostname}")
        print(f"\tHTTP enabled:  {ip_settings['http']['server']}")
        print(f"\tHTTPS enabled:  {ip_settings['http']['secure-server']}")

if __name__ == '__main__':
    main()
