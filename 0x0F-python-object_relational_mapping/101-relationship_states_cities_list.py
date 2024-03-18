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

    results = session.query(State)

    for row in results:
        print(str(row.id) + ':' + row.name)
        for city in row.cities:
            print('\t' + str(city.id) + ':' + city.name)
