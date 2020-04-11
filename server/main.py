#!/usr/bin/env python3

from sys import path
# gives us access to the non-public facing modules
path.append("../private")

from api import zoom, request

request.send_response(200, "Not implemented yet")
