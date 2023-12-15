#!/usr/bin/python3
"""
Script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB_NAME = sys.argv[3]
    db = MySQLdb.connect(user=USER, passwd=PASS, db=DB_NAME)
    cur = db.cursor()
    cur.execute("""SELECT id, name
                FROM states
                WHERE name LIKE %s
                ORDER BY id""", ('N%',))
    all = cur.fetchall()
    for i in all:
        print(i)
