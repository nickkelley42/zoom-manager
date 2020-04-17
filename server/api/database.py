#!/usr/bin/env python3

import mysql.connector
import config
import datetime

def get_user_by_name(name):
    query = "SELECT * FROM `users` WHERE `username`=%s"
    return make_query(query, (name,))

def get_user_by_id(user_id):
    query = "SELECT * FROM `users` WHERE `id`=%s"
    return make_query(query, (user_id,))

def update_password(user_id, hash_data):
    pw = hash_data["key"]
    salt = hash_data["salt"]
    query = """
        UPDATE users
        SET password = %s, salt = %s
        WHERE id = %s
    """
    result = make_query(query, (password, salt, user_id))
    return result

def new_session(user_id, session_id):
    query = ("INSERT INTO sessions (created_at, user_id, id)"
             "VALUES (%s, %s, %s)")
    now = datetime.datetime.now()
    result = make_query(query, (now, user_id, session_id))
    return result

def get_session(session_id):
    query = "SELECT id, user_id, created_at FROM sessions WHERE id=%s"
    result = make_query(query, (session_id,))
    return result

def session_cleanup():
    query = """
        DELETE FROM sessions
        WHERE created_at IS NULL OR created_at < %s
    """
    cutoff = datetime.datetime.now() - datetime.timedelta(hours = 1)
    make_query(query, (cutoff,))

def make_query(query, params=()):
    db_user = config.db_user
    db_host = config.db_host
    db_name = config.db_name
    db_pass = config.db_pass
    cnx = mysql.connector.connect(user=db_user, password=db_pass,
                                  host=db_host, database=db_name)
    cursor = cnx.cursor()
    cursor.execute(query, params)

    keys = cursor.column_names
    vals = cursor.fetchone()
    if vals is None:
        result = None
    else:
        result = dict(zip(keys, vals))

    cnx.commit()
    cursor.close()
    cnx.close()
    return result

