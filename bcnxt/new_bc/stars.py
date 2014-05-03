# coding: utf-8
from core import make_api_url, get_auth, send_request

def get_starred_projects(account_num):
    return send_request(make_api_url(account_num,'stars'),get_auth())
