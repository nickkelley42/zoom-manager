#!/usr/bin/env python3

import json
import cgi
import jwt

response = {}

def send_response(data):
    print("Content-type: application/json\n")
    print(json.dumps(data))

send_response(response)
