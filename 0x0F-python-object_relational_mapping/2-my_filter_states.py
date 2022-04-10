#!/usr/bin/python3
""" Module for task 0-select_states.py """


import MySQLdb
import sys

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE sys.argv[4] IN name ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
            print(row)
            cur.close()
            conn.close()
