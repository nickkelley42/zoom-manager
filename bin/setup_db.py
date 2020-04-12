#!/usr/bin/env python3

import mysql.connector
from os import environ
from hashlib import sha256

create_users_table_query = """
    CREATE TABLE users (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        username VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(64) NOT NULL,
        PRIMARY KEY(id)
    )
"""

create_sessions_table_query = """
    CREATE TABLE sessions (
        id VARCHAR(64) NOT NULL,
        created_at TIMESTAMP ,
        user_id INT UNSIGNED NOT NULL ,
        PRIMARY KEY(id)
    )
"""

db_host = environ["DBHOST"]
db_name = environ["DBNAME"]
db_user = environ["DBUSER"]
db_pass = environ["DBPASS"]
cnx = mysql.connector.connect(user=db_user, database=db_name,
                              host=db_host, password=db_pass)

cur = cnx.cursor(buffered=True)
cur.execute(create_users_table_query)
cur.execute(create_sessions_table_query)

db_salt = environ["DBSALT"]
new_user = "larry"
tmp_pass = "internetcall"
hashed_pass = sha256((db_salt + tmp_pass).encode("utf-8")).hexdigest()

create_first_user_query = """
    INSERT INTO users (username, password)
    VALUES (%s, %s)
"""

cur.execute(create_first_user_query, (new_user, hashed_pass))
cnx.commit()

cnx.close()
