#!/user/bin/env python

# To run: python netconf_schema.py ietf-interfaces
# To print visual representation of ietf-interfaces.yang: pyang -f tree ietf-interfaces.yang

import sys
import yaml
import xml.etree.ElementTree as ET

from ncclient import manager

def main(yang_module):

    # Load the device details from YAML file
    with open('device.yml', 'r') as fp:
        device = yaml.safe_load(fp.read())

    # Retrieve the model from the device
    with manager.connect(**device, hostkey_verify=False) as mgr:

        # Retrieve the model
        schema = mgr.get_schema(yang_module).xml

        # Save the model locally
        with open(yang_module +'.yang', 'w') as out:
            xml_root = ET.fromstring(schema)
            yang_content = list(xml_root)[0].text
            out.write(yang_content)

if __name__ == '__main__':
    main(sys.argv[1])    # sys.argv is used to accept the module name at run time