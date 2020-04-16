#!/usr/bin/env python3

import hashlib
import os

def check_hash(password, salt, known):
    check = hashalg(password, salt)
    return check == known

def generate_hash(password):
    salt = generate_salt()
    key = hashalg(password, salt)
    return { 'key': key, 'salt': salt }

def generate_salt():
    return os.urandom(32)

def hashalg(password, salt):
    return hashlib.pbkdf2_hmac(
        'sha512',
        password.encode('utf-8'),
        salt,
        100000
    )

