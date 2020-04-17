#!/usr/bin/env python3

import mysql.connector
import config
from lib.hashing import generate_hash

query = """
    INSERT INTO users (username, password, salt)
    VALUES (%s, %s, %s)
"""

username = input("Enter username: ")
password = input("Enter password: ")

hashed = generate_hash(password)
hashed_pass = hashed["key"]
salt = hashed["salt"]

db_host = config.db_host
db_name = config.db_name
db_user = config.db_user
db_pass = config.db_pass
cnx = mysql.connector.connect(user=db_user, database=db_name,
                              host=db_host, password=db_pass)

cur = cnx.cursor(buffered=True)
cur.execute(query, (username, hashed_pass, salt))

cnx.commit()
cnx.close()

print("Success")
