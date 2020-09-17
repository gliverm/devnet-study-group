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

    with manager.connect(**device, hostkey_verify=False) as mgr:

        # edit-config call to the running datastore
        resp = mgr.edit_config(target='running', config=IPv4_acl_payload)
        if resp.ok:
            print('ACL was successfully created.')
        else:
            print(f'ACL could not be created.\n{resp}')

if __name__ == '__main__':
    main()