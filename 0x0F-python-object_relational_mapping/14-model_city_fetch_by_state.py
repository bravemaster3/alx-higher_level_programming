#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    from model_state import Base, State
    from model_city import City
    import sqlalchemy
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker, relationship
    import sys

    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB_NAME = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        USER, PASS, DB_NAME), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    all_rows = session.query(City, State).join(State).all()

    for i in all_rows:
        print("{}: ({}) {}".format(i.State.name, i.City.id, i.City.name))

    session.close
