#!/user/bin/env python

import yaml
import xmltodict
from ncclient import manager

# Define a filter using <filter> tag to
# retrieve the openconfig-interfaces model
INTERFACE_STATE_XML = """
<filter>
  <interfaces xmlns="http://openconfig.net/yang/interfaces">
    <interface>
      <state/>
    </interface>
  </interfaces>
</filter>
"""

def main():

    with open('device.yml', 'r') as fp:
        device = yaml.safe_load(fp.read())

    # Connect
    with manager.connect(**device, hostkey_verify=False) as mgr:

        # Use .get() to retrieve the configuration using a filter
        resp = mgr.get(INTERFACE_STATE_XML).xml

        # Load the xml response data as a Python dict
        resp_dict = xmltodict.parse(resp)
        interfaces = resp_dict.get('rpc-reply')['data']['interfaces']['interface']

        # Display operational for interfaces
        for iface in interfaces:
            state = iface['state']

            if state['oper-status'] == 'UP':
                name = state['name']
                counters = state['counters']
                in_packets = int(counters['in-unicast-pkts'])
                out_packets = int(counters['out-unicast-pkts'])

                print(f'Interface: {name}')
                print(f'\tInput Packets:  {in_packets}')
                print(f'\tOutput Packets:  {out_packets}')
                print(f'\tTotal Packets:  {in_packets + out_packets}')

if __name__ == "__main__":
    main()
