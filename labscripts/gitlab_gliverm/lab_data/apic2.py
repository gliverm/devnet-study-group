#!/usr/bin/env python
import requests

def login(host, username, password):
    ''' Login to the APIC and return a session token '''

    login_uri = f"https://{host}/api/aaaLogin.json"
    login_body = {'aaaUser':{'attributes':{'name': username, 'pwd':password}}}

    session = requests.session()
    session.verify = False

    r = session.post(login_uri, json=login_body)

    return (r.json()['imdata'][0]['aaaLogin']['attributes']['token'])


def create_tenant(host, tname, token):
    '''
    create new tenant

    Parameters:
    host (str) - hostname or IP address of APIC
    tname (str) - name of the tenant to create
    token (str) - authentication token
    '''

    tenant_uri = f'https://{host}/api/mo/uni.json'
    tenant_body = {'fvTenant': {
        'attributes':{
            'name': tname,
        }
    }
    }

    cookie = {'APIC-cookie':token}
    session = requests.session()
    session.verify = False
    r = session.post(tenant_uri, json=tenant_body, cookies=cookie)

    return r.json()

def get_tenant(host, tname, token):
    '''
    retrieve the tenant objecf

    Parameters:
    host (str) - hostname or IP address of APIC
    tname (str) - name of the tenant to create
    token (str) - authentication token
    '''

    tenant_uri = f'https://{host}/api/mo/uni/tn-{tname}.json'
    cookie = {'APIC-cookie': token}
    session = requests.session()
    session.verify = False
    r = session.get(tenant_uri, cookies=cookie)

    return r.json()
