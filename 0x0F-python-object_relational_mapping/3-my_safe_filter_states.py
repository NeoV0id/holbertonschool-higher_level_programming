#!/usr/bin/python3
""" Module for task 3 """


import MySQLdb
import sys


if __name__ == '__main__':

    conn = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            passwd='', db=sys.argv[3], charset="utf8")

    cur = conn.cursor()
    cur.execute(
            "SELECT * FROM 'states' WHERE 'name' IN '{}'\
            ORDER BY 'states'.'id' ASC".format(sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
        cur.close()
        conn.close()
