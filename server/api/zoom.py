#!/usr/bin/env python3

import jwt
import config
import datetime
import http.client
import json
from random import randint

def get_meetings():
    uid = _get_uid()
    url = '/users/{}/meetings'.format(uid)
    data = _zoom_api_request(url)
    return data['meetings']

def get_meeting(id):
    url = '/meetings/{}'.format(id)
    data = _zoom_api_request(url)
    return data

def create_meeting(topic, start_string, pw=None):
    uid = _get_uid()
    url = '/users/{}/meetings'.format(uid)
    
    data = {
        'topic': topic,
        'start_time': start_string
    }
    if pw is not None:
        data['password'] = pw
    else:
        data['password'] = str(randint(1000, 9999))

    new_meeting = _zoom_api_request(url=url, method='POST', body=data)
    return new_meeting

def _get_uid():
    url = '/users?status=active'
    data = _zoom_api_request(url)
    user = data['users'][0]
    return user['id']

def _get_jwt():
    return jwt.encode(
        {
            'iss': config.zoom_api_key,
            'exp': _expiration()
        },
        config.zoom_api_secret,
        algorithm = 'HS256'
    ).decode()
    
def _expiration():
    # 1 minute from now
    return datetime.datetime.utcnow() + datetime.timedelta(minutes = 1)

def _zoom_api_request(url, method='GET', body=None):
    con = http.client.HTTPSConnection('api.zoom.us')

    prefixed = '/v2' + url
    headers = {
        'authorization': 'Bearer {}'.format(_get_jwt()),
        'content-type': 'application/json'
    }
    if body is None:
        json_body = None
    else:
        json_body = json.dumps(body)

    con.request(method, prefixed, headers=headers, body=json_body)

    res = con.getresponse()
    data = res.read()
    return json.loads(data)

