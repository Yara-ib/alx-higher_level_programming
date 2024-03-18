#!/usr/bin/python3
"""
    Script that creates the State “California” with
    the City “San Francisco” from the database hbtn_0e_100_usa
"""
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True
        )

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    new_state = State('California')

    new_city = City('San Francisco')
    new_state.cities.append(new_city)
    session.add(new_state)

    session.commit()
