#!/usr/bin/env python

import apic
from pprint import pprint

def main():
    '''
    Point of entry for apic_delete_tenant.
    '''
    apic_info = {
    'host': '192.168.2.149',
    'username': 'admin',
    'password': 'WWTwwt1!'
    }
    tenant_name = 'new-tenant'

    results = apic.delete_tenant(apic_info['host'], tenant_name, apic.login(**apic_info))

    pprint(results)

if __name__ == "__main__":
    main()