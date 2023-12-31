#!/usr/bin/python3
""" class that inherit from BaseModel """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ class definition of amenity 
    class attribute __tablename__
    represents the table name, amenities
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
