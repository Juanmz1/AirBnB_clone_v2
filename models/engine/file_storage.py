#!/usr/bin/python3
import json
import os
import datetime
"""
FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances:
"""
class FileStorage:
    """ A fileStorage class """
    __file_path = "json.file"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with
        key <obj class name>.id
        """
        key = [f"{obj.__class__.__name__}.{obj.id}"]
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the
        JSON file (path: __file_path)
        """
        dict_obj = {}
        for key, value in self.__objects.items():
            dict_obj[key] = values.to_dict()
            with open(self.__file_path, "w", encoding = "utf-8") as Jsonfil:
                json.dump(dict_obj, Jsonfil)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding = "utf-8") as Jsonfil:
                dict_obj2 = json.load(Jsonfil)
                for key, values in dict_obj2.items():
                    dict_obj2 = {key: self.classes()[values["__class__"]](**v)}
                self.__objects = dict_obj2

    def classes(self):
        """
        return the dictionary of a valid classes
        """
        from models.base_model import BaseModel

        classes = {"BaseModel": BaseModel
                }
        return classes

    def attributes(self):
        """
        return the valid attributes
        """
        attributes = {
                "BaseModel":
                        {"id": str,
                        "created_at": datetime.datetime,
                        "updated_at": datetime.datetime}
                        }
        return attributes
