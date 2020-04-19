#!/usr/bin/env python3

from sys import path
# gives us access to the non-public facing modules
path.append("../private")

import request
import auth
import meetings
import re
from os import environ

response = request.Response()

unauth_routes = {
    "^/api/login/?$": auth.login,
    "^/api/auth-test/?$": auth.auth_test,
}

auth_routes = {
    "^/api/update-pass/?$": auth.change_password,
    "^/api/meetings": meetings.meetings_actions,
}

def find_handler(routes, url):
    for route, handler in routes.items():
        if re.match(route, url):
            return handler
    return False

url = environ["REQUEST_URI"]
handler = False

authenticated = auth.is_authenticated()

if authenticated:
    handler = find_handler(auth_routes, url)
if not handler:
    handler = find_handler(unauth_routes, url)

if handler:
    handler()
else:
    response = request.Response()
    if authenticated:
        response.status = 404
        response.data = "not found"
    else:
        response.status = 403
        response.data = "not logged in"

    response.send()
