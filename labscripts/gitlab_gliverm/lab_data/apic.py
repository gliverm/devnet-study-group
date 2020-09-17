#!/usr/bin/env python

import requests

def login(host, username, password):
    '''
    Login to the APIC and return a session token
    APIC = Cisco Application Policy Infrastructure Controller

    Parameters:
    host(str) - hostname or IP address of APIC
    username (str) - username for authentication
    password (str) - password for authentication
    '''

    # Note: in this particular API the .json indicates the accept format which
    #   in other APIs is indicated with a header value.  APIC ignores the accept
    #   if present in a header.
    login_uri = f"https://{host}/api/aaaLogin.json"
    login_body = {'aaaUser':{'attributes':{'name': username, 'pwd':password}}}

    # Create a session for cookie persistence, connection pooling, and configuration
    session = requests.session()
    session.verify = False

    r = session.post(login_uri, json=login_body)

    return (r.json()['imdata'][0]['aaaLogin']['attributes']['token'])

def create_tenant(host, tname, token):
    '''
    Create new tenant

    Parameters:
    host (str) - hostname or IP address of APIC
    tname (str) - name of the tenant to create
    token (str) - authentication token
    '''

    tenant_uri = f'https://{host}/api/mo/uni.json'
    tenant_body = {'fvTenant': {'attributes': {'name': tname}}}

    cookie = {'APIC-cookie':token}
    session = requests.session()
    session.verify = False  # requred because this lab does not have trusted certificates   
    r = session.post(tenant_uri, json=tenant_body, cookies=cookie)

    return r.json()

def get_tenant(host, tname, token):
    '''
    Retrieve the tenant object

    Parameters:
    host (str) - hostname or IP address of APIC
    tname (str) - name of the tenant to create
    token (str) - authentication otken
    '''
    tenant_uri = f'https://{host}/api/mo/uni/tn-{tname}.json'
    cookie = {'APIC-cookie': token}
    # Create session and instruct it not to validate the certificate
    session = requests.session()
    session.verify = False
    r = session.get(tenant_uri, cookies=cookie)
    return r.json()

def delete_tenant(host, tname, token):
    '''
    Delete the tenant object

    Parameters:
    host (str) - hostname or IP address of APIC
    tname (str) - name of the tenant to create
    token (str) - authentication otken
    '''

    tenant_uri = f'https://{host}/api/mo/uni/tn-{tname}.json'
    cookie = {'APIC-cookie': token}
    session = requests.session()
    session.verify = False
    r = session.delete(tenant_uri, cookies=cookie)
    return r
