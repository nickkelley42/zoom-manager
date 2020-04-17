#!/usr/bin/env python3

import jwt
import config
import datetime
import http.client
import json

def get_meetings():
    uid = _get_uid()
    url = '/users/{}/meetings'.format(uid)
    data = _zoom_api_request(url)
    return data['meetings']

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

def _zoom_api_request(url):
    con = http.client.HTTPSConnection('api.zoom.us')

    prefixed = '/v2' + url
    headers = {
        'authorization': 'Bearer {}'.format(_get_jwt()),
        'content-type': 'application/json'
    }
    con.request('GET', prefixed, headers=headers)

    res = con.getresponse()
    data = res.read()
    return json.loads(data)

