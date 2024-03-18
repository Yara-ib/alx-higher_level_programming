#!/usr/bin/python3
"""
    Script that lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa
"""
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True
        )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # results = session.query(State).order_by(State.id)

    # for row in results:
    #     print(str(row.id) + ':' + row.name)
    #     for city in row.cities:
    #         print('\t' + str(city.id) + ':' + city.name)
    results = session.query(State).order_by(State.id)
    for row in results:
        print(f"{row.id}: {row.name}")
        for city in row.cities:
            print(f"\t{city.id}: {city.name}")
