#!/usr/bin/python3
""" Class definition of a State """
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ State Class """
    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(128), nullable=False)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.id}: {self.name}"
