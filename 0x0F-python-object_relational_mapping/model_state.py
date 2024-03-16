#!/usr/bin/python3
""" Class definition of a State """
from sqlalchemy import Integer, String, CHAR, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


if __name__ == "__main__":
    Base = declarative_base()

    class State(Base):
        """ State Class """
        __tablename__ = 'states'
        id = Column('id', Integer, primary_key=True)
        name = Column('name', String(128), nullable=False)
