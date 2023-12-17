#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_101_usa
"""

if __name__ == "__main__":
    from relationship_city import City
    from relationship_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB_NAME = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        USER, PASS, DB_NAME), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).order_by(State.id).all()
    for state in all_states:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))

    session.commit()
    session.close()
