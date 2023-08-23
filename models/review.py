#!/usr/bin/python3
""" contain class inherit from basemodel """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey

class Review(BaseModel, Base):
    """ class definition of the review """
    __tablename__ = 'rewiews'
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
