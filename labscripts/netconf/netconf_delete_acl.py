#!/usr/bin/env python

import yaml
from ncclient import manager

payload = """
<config>
  <acl xmlns="http://openconfig.net/yang/acl">
   <acl-sets>
      <acl-set operation="delete">
        <name>TEST</name>
        <type>ACL_IPV4</type>
      </acl-set>
   </acl-sets>
  </acl>
</config>
"""

def main():
     
    # Load the device deails from YAML file
    with open('device.yml', 'r') as fp:
        device = yaml.safe_load(fp.read())

    # Connect
    with manager.connect(**device, hostkey_verify=False) as mgr:

        # Check whether the candidate capability is supported
        if ':candidate' in mgr.server_capabilities:

            # Lock the running and canddiate datastores
            with mgr.locked('running'), mgr.locked('candidate'):

                # Delete candidate datastore
                resp = mgr.edit_config(target='candidate',
                                       config=payload,
                                       default_operation="none")
                # if resp.ok:
                #     print('succesfully deleted configuration.')

                #Commit the change if it's successful
                if resp.ok:
                    # Commit the change to running-config
                    print('committing config to running...')
                    commit_resp = mgr.commit()
                    # TODO What happens if commit does not take?
                    if commit_resp.ok:
                        print('config successfully committed.')
                else:
                    print('config could not be deployed')
                
        else:
            print(':candidate capability does nto appear to be supported.')

if __name__ == '__main__':
    main()