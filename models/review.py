#!/usr/bin/python3
""" contain class inherit from basemodel """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel):
    """ class definition of the review """
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
