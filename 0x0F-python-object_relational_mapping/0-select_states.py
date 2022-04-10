#!/usr/bin/python3
""" Module for task 0-select_states.py """


import MySQLdb
import sys


if __name__ == '__main__':

    conn = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
        cur.close()
        db.close()
