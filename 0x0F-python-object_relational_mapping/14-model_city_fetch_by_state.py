#!/usr/bin/python3
"""
    Script that prints all City objects from the database hbtn_0e_14_usa
"""
from model_state import State
from model_city import City
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

    results = session.query(City, State).join(City).order_by(City.id)

    for state, city in results:
        print(f"{city.name}: ({state.id}) {state.name}")
