#!/usr/bin/env python3

from os import environ
from http import cookies
import datetime
import config
from hashlib import sha256
import database
import request
from datetime import datetime
import forms

def is_authenticated():
    cookie = get_cookie()
    if "session" not in cookie:
        return False
    session_id = cookie["session"].value
    session = database.get_session(session_id)
    return session is not None

def auth_test():
    response = request.Response()
    if is_authenticated():
        response.data = "Logged in"
    else:
        response.data = "Not logged in"
    response.send()

def login():
    response = request.Response()

    data = forms.get_form_data()
    if "username" not in data or "password" not in data:
        login_failure(response, "bad form data")

    username = data["username"]
    password = data["password"]

    user = database.get_user(username)
    if not user:
        login_failure(response, "no matching user")
        return

    correct = user["password"]
    check = hash(password)

    if not check == correct:
        login_failure(response, "wrong password")
        return

    new_session(response, user)

def new_session(response, user, message="success"):
    new_session_id = hash(str(datetime.now()) + user["username"])
    session = database.new_session(user["id"], new_session_id)
    set_cookie(response, "session", new_session_id)
    response.data = message
    response.send()
    

def login_failure(response, message="failure"):
    response.status = 401
    response.data = message
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
    salted = config.db_salt + text
    return sha256(salted.encode("utf-8")).hexdigest()

