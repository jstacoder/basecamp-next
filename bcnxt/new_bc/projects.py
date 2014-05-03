# coding: utf-8
from core import make_api_url, send_request, get_auth

AUTH = get_auth()

def get_all_active_projects(account_num):
    return send_request(make_api_url(account_num,'projects'),AUTH)

def get_all_archived_projects(account_num):
    return send_request(make_api_url(account_num,'projects','archived'),AUTH)

def get_project(account_num,project_id):
    return send_request(make_api_url(account_num,'projects',project_id),AUTH)

