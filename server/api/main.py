#!/usr/bin/env python3

from sys import path
# gives us access to the non-public facing modules
path.append("../private")

import zoom
import request
import auth

if auth.is_authenticated():
    request.send_response(200, "Not implemented")
else:
    request.send_response(401, "Not logged in")
