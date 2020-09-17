import yaml
from ncclient import manager

# XML formatted payload to create the ACL.
# Note to self: when do templates come into play?  Jinja2
IPv4_acl_payload = """
<config>
    <acl xmlns="http://openconfig.net/yang/acl">
    <acl-sets>
        <acl-set>
        <name>TEST</name>
        <type>ACL_IPV4</type>
        <config>
            <name>TEST</name>
            <type>ACL_IPV4</type>
        </config>
        <acl-entries>
            <acl-entry>
            <sequence-id>10</sequence-id>
            <config>
                <sequence-id>10</sequence-id>
            </config>
            <ipv4>
                <config>
                <source-address>10.10.10.1/32</source-address>
                <destination-address>20.20.20.1/32</destination-address>
                <protocol>6</protocol>
                </config>
            </ipv4>
            <actions>
                <config>
                <forwarding-action>ACCEPT</forwarding-action>
                </config>
            </actions>
            </acl-entry>
        </acl-entries>
        </acl-set>
    </acl-sets>
    </acl>
</config>
"""

def main():

    with open('device.yml', 'r') as fp:
        device = yaml.safe_load(fp.read())

    # Connect
    with manager.connect(**device, hostkey_verify=False) as mgr:
        if ':candidate' in mgr.server_capabilities:

            # Discard any uncommitted changes in the candidate ds
            mgr.discard_changes()

            # Lock the runnign and candidate datastores
            with mgr.locked('running'), mgr.locked('candidate'):

                # Push the new change to the device
                print('updating candidate config...')
                resp = mgr.edit_config(target='candidate', config=IPv4_acl_payload)
                
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
            print(':candidate capability does not appear to be supported')

if __name__ == '__main__':
    main()