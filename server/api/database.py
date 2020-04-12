#!/usr/bin/env python3

import mysql.connector
import config

def get_user(username):
    query = "SELECT * FROM users WHERE 'username'=%s"
    result = make_query(query, (username))
    return result

def new_session(user_id, session_id):
    query = ("INSERT INTO sessions (user_id, id)"
             "VALUES (%s, %s)")
    result = make_query(j)
    return result

def get_session(session_id):
    query = "SELECT id, user_id, created_at FROM sessions WHERE id=%s"
    result = make_query(query, (session_id))
    return result

def make_query(query, params=()):
    db_user = config.db_user
    db_host = config.db_host
    db_name = config.db_name
    db_pass = config.db_pass
    cnx = mysql.connector.connect(user=db_user, password=db_pass,
                                  host=db_host, database=db_name)
    cursor = cnx.cursor()
    cursor.execute(query, params)
    results = []
    for row in cursor:
        results.append(row)
    cursor.close()
    cnx.close()
    return results
