#!/usr/bin/python3
import json
import os
import datetime
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""
FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances:
"""


class FileStorage:
    """ A fileStorage class """
    __file_path = "json.file"
    __objects = {}

    def all(self, cls:None):
        """
        returns the dictionary __objects
        """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    cls_dict[key] = value
            return cls_dict
        return self.__objects
        """ return FileStorage.__objects"""

    def new(self, obj):
        """
        sets in __objects the obj with
        key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the
        JSON file (path: __file_path)
        """
        dict_obj = {}
        for key, values in FileStorage.__objects.items():
            dict_obj[key] = values.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as Jsonfil:
            json.dump(dict_obj, Jsonfil)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        from models.base_model import BaseModel
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as Jsonfil:
                dict_obj2 = json.load(Jsonfil)
                for key in dict_obj2.keys():
                    dict_1 = dict_obj2[key]["__class__"]
                    obj = eval(dict_1)(**dict_obj2[key])
                    self.__objects[key] = obj

    def delete(self, obj=None):
        """ new public instance method to delete """
        if obj is None:
            return
        key = "{}.{}".format(type(obj).__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]

    def close(self):
        """ reload method call back """
        self.reload()
