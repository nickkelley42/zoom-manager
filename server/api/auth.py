#!/usr/bin/env python3

from os import environ
from http import cookies
import datetime
import config
import database
import request
from datetime import datetime
import forms
from lib import hashing

def is_authenticated():
    session = get_session()
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
        login_failure(response)

    username = data["username"]
    password = data["password"]

    user = database.get_user_by_name(username)
    if not user:
        login_failure(response)
        return

    known = user["password"]
    salt = user["salt"]
    password = data["password"]
    success = hashing.check_hash(password, salt, known)

    if not success:
        login_failure(response)
        return

    new_session(response, user)

def new_session(response, user, message="success"):
    new_session_id = hashing.new_session_id()
    session = database.new_session(user["id"], new_session_id)
    set_cookie(response, "session", new_session_id)
    response.data = message
    response.send()

def get_session():
    cookie = get_cookie()
    if "session" not in cookie:
        return None
    session_id = cookie["session"].value
    session = database.get_session(session_id)
    return session

def login_failure(response, message="failure"):
    response.status = 401
    response.data = message
    response.send()

def change_password():
    response = request.Response()
    data = forms.get_form_data()
    if "old" not in data or "new" not in data:
        login_failure(response)
        return
    
    session = get_session()
    user_id = session["user_id"]
    user = database.get_user_by_id(user_id)

    current = user["password"]
    salt = user["salt"]
    maybe = data["old"]
    correct_pw = hashing.check_hash(maybe, salt, current)

    if not correct_pw:
        login_failure(response)
        return

    hash_data = hashing.generate_hash(data["new"])
    database.update_password(user_id, hash_data)

    response.data = "success"
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

