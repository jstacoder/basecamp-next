'''
    new_bc.core.py

    core api calls for new_bc api library
'''
import os
import requests as req

API_URL = 'https://basecamp.com/{}/api/v1/'

def make_api_url(account_num,call,*args):
    u = API_URL.format(account_num) + call 
    u = u + '.json' if not args else u + '/' + '/'.join(map(str,args)) + '.json'
    return u

def send_request(url,auth):
    return req.get(url,auth=auth).json()

def get_auth():
    if os.path.exists('auth.txt'):
        return tuple([str(x[:-1]) for x in tuple(open('auth.txt','r').readlines())])
