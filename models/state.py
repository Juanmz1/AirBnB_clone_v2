#!/usr/bin/python3
""" state class that inherit from baseModel """
import models
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City

class State(BaseModel, Base):
    """ class definition of state
    class attribute __tablename__
    represents the table name, states
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            list_city = []
            for city in list(models.storage.all(City).values()):
                if states.id == self.id:
                    list_city.append(city)
            return list_city
