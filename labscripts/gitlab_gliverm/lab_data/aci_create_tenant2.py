#!/usr/bin/env python

def main():

    import apic2 as apic

    apic_info = {
        'host': '192.168.2.149',
        'username': 'admin',
        'password': 'WWTwwt1!'
    }
    tenant_name = 'new-tenant'

    results = apic.create_tenant(
    apic_info['host'], tenant_name, apic.login(**apic_info))

    print(results)

if __name__ == "__main__":
    main()