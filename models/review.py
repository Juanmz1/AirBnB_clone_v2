#!/usr/bin/python3
""" contain class inherit from basemodel """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel):
    """ class definition of the review """
    place_id = Column(String(60), nullable=False, ForeignKey=("places.id"))
    user_id = Column(String(60), nullable=False, ForeignKey=("users.id"))
    text = Column(String(1024), nullable=False)
