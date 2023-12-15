#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB_NAME = sys.argv[3]
    db = MySQLdb.connect(user=USER, passwd=PASS, db=DB_NAME)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                ORDER BY id""")
    all = cur.fetchall()
    for i in all:
        print(i)
