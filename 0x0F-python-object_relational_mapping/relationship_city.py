#!/usr/bin/python3
""" Class definition of City """
from relationship_state import Base, State
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class City(Base):
    """ City Class """
    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column(
        'state_id', Integer, ForeignKey('states.id'), nullable=False
        )
    state = relationship("State", backref="cities")

    def __init__(self, name, *args, **kwargs):
        self.name = name

    def __str__(self):
        return f"{self.id}: {self.name}"
