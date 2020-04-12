#!/usr/bin/env python

from os import environ
from http import cookies
import datetime
import config
from hashlib import sha256
import database
import request
from datetime import now

def is_authenticated():
    cookie = get_cookie()
    if "session" not in cookie:
        return False
    session_id = cookie["session"].value
    session = database.get_session(session_id)
    return len(session) > 0

def login():
    response = request.Response()

    # placeholders, so the script runs, but always fails
    username = ""
    password = ""

    user = database.find_user(username)
    if not user:
        login_failure(response)
        return

    correct = user["password"]
    check = hash(password)

    if not check == correct:
        login_failure(response)
        return

    new_session_id = hash(str(datetime.now()) + username)
    try:
        session = database.new_session(new_session_id)
        set_cookie(response, "session", session)
        response.data = "success"
        response.send()
    except:
        login_failure(response)

def login_failure(response):
    response.status = 401
    response.data = "failure"
    response.send()

def get_cookie():
    cookie = cookies.SimpleCookie()
    if "HTTP_COOKIE" in environ:
        cookie.load(environ["HTTP_COOKIE"])
    return cookie

def set_cookie(response, name, value):
    cookie = cookies.SimpleCookie()
    cookie[name] = value
    cookie[name]["secure"] = True
    response.add_header(cookie)

def hash(text):
    salted = config.salt + text
    return sha256(salted.encode("utf-8")).hexdigest()

def salt(text):
    salt = config.salt
    return salt + text
