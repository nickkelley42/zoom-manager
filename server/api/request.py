#!/usr/bin/env python3

import cgi
import json

def send_response(status, data):
    print("Content-type: application/json\n")
    print(json.dumps(data))
