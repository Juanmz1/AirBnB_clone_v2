#!/usr/bin/python3
""" BaseModel that defines all common attributes/methods for other classes: """
from uuid import uuid4
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime

Base = declarative_base()


class BaseModel:
    """
    A class of the base model
    """
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        initialization of the baseModel
        you will use *args,
        **kwargs arguments for the constructor of a BaseModel
        """
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            for key, values in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    values = datetime.strptime(values, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, values)

    def __str__(self):
        """
        string representation of the object
        """
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, repr(self.__dict__))

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dict_obj = {}
        for key, values in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                dict_obj[key] = values.isoformat()
            else:
                dict_obj[key] = values
        dict_obj["__class__"] = type(self).__name__
        if "_sa_instance_state" in dict_obj:
            del dict_obj["_sa_instance_state"]
        return dict_obj

    def delete(self):
        """ to delete the current storage """
        models.stroage.delete(self)
