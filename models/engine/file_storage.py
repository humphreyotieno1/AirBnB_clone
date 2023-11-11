#!/usr/bin/python3
"""Define FileStorage class"""
import json
import os
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """Class serializes instances to JSON file and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}
    classes = {"BaseModel": BaseModel, "User": User}

    def all(self):
        """Returns dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects to a JSON file"""
        objects_dict = {}
        for key, value in FileStorage.__objects.items():
            objects_dict[key] = value.to_dict()
        
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Deserialize objects from a JSON file"""
        try:
            with open(self.__file_path, 'r') as f:
                new_objects = json.load(f)
                for key, val in new_objects.items():
                    class_name = val['__class__']
                    class_type = globals()[class_name]
                    obj = class_type(**val)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
