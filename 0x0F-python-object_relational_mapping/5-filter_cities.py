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
    STATE = sys.argv[4]
    db = MySQLdb.connect(user=USER, passwd=PASS, db=DB_NAME)
    cur = db.cursor()
    cur.execute("""SELECT cities.name, states.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id""", (STATE,))
    all = cur.fetchall()
    all_len = len(all)
    for i in range(all_len):
        if i == all_len - 1:
            print(all[i][0])
        else:
            print(all[i][0], end='')
    print()
