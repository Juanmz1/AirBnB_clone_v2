#!/usr/bin/python3
""" Class that inherit from Basemodel """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ class definition of City 
    class attribute __tablename__ -
    represents the table name, cities
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, Foreignkey=("states.id"))
    places = relationship("Place", backref="user", cascade="delete")
