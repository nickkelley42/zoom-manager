#!/usr/bin/env python3

import jwt
import config
import datetime
import http.client
import json

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

    headers = {
        'authorization': 'Bearer {}'.format(_get_jwt()),
        'content-type': 'application/json'
    }
    con.request('GET', url, headers=headers)

    res = con.getresponse()
    data = res.read()
    return json.loads(data)

