#!/usr/bin/env python3

import mysql.connector
import config

create_users_table_query = """
    CREATE TABLE users (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        username VARCHAR(100) NOT NULL UNIQUE,
        password VARBINARY(64) NOT NULL,
        salt VARBINARY(64) NOT NULL,
        PRIMARY KEY(id)
    )
"""

create_sessions_table_query = """
    CREATE TABLE sessions (
        id VARCHAR(128) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        user_id INT UNSIGNED NOT NULL ,
        PRIMARY KEY(id)
    )
"""

db_host = config.db_host
db_name = config.db_name
db_user = config.db_user
db_pass = config.db_pass
cnx = mysql.connector.connect(user=db_user, database=db_name,
                              host=db_host, password=db_pass)

cur = cnx.cursor(buffered=True)
cur.execute(create_users_table_query)
cur.execute(create_sessions_table_query)

#db_salt = config.db_salt
#new_user = "larry"
#tmp_pass = "internetcall"
#salted = db_salt + tmp_pass
#hashed_pass = sha256(salted.encode("utf-8")).hexdigest()
#
#create_first_user_query = """
#    INSERT INTO users (username, password)
#    VALUES (%s, %s)
#"""
#
#cur.execute(create_first_user_query, (new_user, hashed_pass))

cnx.commit()

cnx.close()
