#!/usr/bin/python3
"""
    Script that lists all City objects
    from the database hbtn_0e_101_usa
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

    results = session.query(City).order_by(City.id)

    for row in results:
        print(f"{row.id}: {row.name}-> {row.state.name}")
