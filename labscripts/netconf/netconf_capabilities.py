#!/usr/bin/env python

# manager class allows creation of manager object to use as a higher
#   level API to connect to and interact with the YANG models on the device
from ncclient import manager

device = {
    'host': 'r1.lab.local',
    'username': 'wwt',
    'password': 'WWTwwt1!',
    'port': 830
}

def main():
    # # Connect to the device using the manager object
    # mgr = manager.connect(
    #     host=device['host'],
    #     username=device['username'],
    #     password=device['password'],
    #     port=device['port'],
    #     hostkey_verify=False
    # )

    # # Display Capabilities advertised by the device(server)
    # for capability in mgr.server_capabilities:
    #     print(capability)

    # # Close the netconf session
    # mgr.close_session()

    # Refactor to use context manager
    # Double *'s infront of dict gives keyword arguments
    # Single * gives you all functional parameters as a tuple or to unpack a list
    # More reading on context manager is that a class needs to have an 
    #   __enter__ and __exit_ method define
    with manager.connect(**device, hostkey_verify=False) as mgr:
        for capability in mgr.server_capabilities:
            print(capability)

if __name__ == "__main__":
    main()

