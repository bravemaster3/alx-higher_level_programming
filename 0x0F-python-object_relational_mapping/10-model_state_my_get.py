#!/usr/bin/python3
"""
Script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from model_state import Base, State
    import sqlalchemy
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    import sys

    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB_NAME = sys.argv[3]
    STATE = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        USER, PASS, DB_NAME), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).filter(State.name == STATE)

    if rows.count() > 0:
        for i in rows:
            print(i.id)
    else:
        print("Not found")

    session.close
