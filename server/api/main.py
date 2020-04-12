#!/usr/bin/env python

from sys import path
# gives us access to the non-public facing modules
path.append("../private")

import request
import auth
import re
from os import environ

response = request.Response()

unauth_routes = {
    "^/api/login/?$": auth.login
}

auth_routes = {}

def find_handler(routes, url):
    for route, handler in routes.items():
        if re.match(route, url):
            return handler
    return False

url = environ["REQUEST_URI"]
handler = False

if auth.is_authenticated():
    handler = find_handler(auth_routes, url)
if not handler:
    handler = find_handler(unauth_routes, url)

if handler:
    handler()
else:
    response = request.Response()
    response.status = 400
    response.data = "Bad request"
    response.send()
