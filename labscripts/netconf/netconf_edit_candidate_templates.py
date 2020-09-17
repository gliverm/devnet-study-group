#!/usr/bin/env python

import yaml
from ncclient import manager
from netconf_templates import CREATE_OC_IPV4_ACL  # Import the Jinja2 template
from jinja2 import BaseLoader, Environment, Template

def render_template(templateIO, data):
    '''
    Render a Jinja template with supplied data

    Parameters:
        templateIO (str): jinja2 formatted string template
        data (dict): data to be rendered to template

    Returns:
        str: rendered string
    '''
    env = Environment(
        loader=BaseLoader(),
        trim_blocks=True,
        lstrip_blocks=True
    )
    template = Template(templateIO)
    return template.render(acl_sets=data)

def main():

    with open('device.yml', 'r') as fp:
        device = yaml.safe_load(fp.read())

    # Load Data
    with open('acls.yml', 'r') as fp:
        ACL_DATA = yaml.safe_load(fp.read())
        print(ACL_DATA)

    # Connect
    with manager.connect(**device, hostkey_verify=False) as mgr:
        if ':candidate' in mgr.server_capabilities:

            # Discard any uncommitted changes in the candidate ds
            mgr.discard_changes()

            # Lock the runnign and candidate datastores
            with mgr.locked('running'), mgr.locked('candidate'):

                # Create Payload
                print('creating ACL payload...')
                payload = render_template(CREATE_OC_IPV4_ACL, ACL_DATA)

                # Push the new change to the device
                print('updating candidate config...')
                resp = mgr.edit_config(target='candidate', config=payload)
                
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