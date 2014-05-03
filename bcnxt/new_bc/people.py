# coding: utf-8
from core import send_request,make_api_url, get_auth

def get_all_people(account_num):
    return send_request(make_api_url(account_num,'people'),get_auth())

def get_person(account_num,person_id):
    return send_request(make_api_url(account_num,'people',person_id),get_auth())

def get_me(account_num):
    return send_request(make_api_url(account_num,'people','me'),get_auth())
