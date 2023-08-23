#!/usr/bin/python3
""" class inherit from the BaeModel """
from os import getenv
import models
from models.base_model import BaseModel
from models.base_model import Base
import sqlalchemy
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import Table
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import relationship


if getenv("HBNB_TYPE_STORAGE") == 'db':
    place_amenity = Table("place_amenity", Base.metadata,
                    Column("place_id", String(60), ForeignKey("places.id"),
                           primary_key=True, nullable=False),
                    Column("amenity_id", String(60), ForeignKey("amenities.id"),
                           primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ class definition of Place
    class attribute __tablename__
    represents the table name, places
    """
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(128), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def review(self):
            """ list of all review"""
            list_review = []
            for review in list(models.storage.all(Review).values()):
                if place.id == self.id:
                    list_review.append(review)
            return list_review

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def amenities(self):
            """ return a list of amenities"""
            list_amenities = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id == self.amenity_ids:
                    list_amenities.append(amenity)
            return list_amenities

        @amenities.setter
        def amenities(self, value):
            """ handle the append method """
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)

