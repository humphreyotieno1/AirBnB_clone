#!/usr/bin/python3
"""Define FileStorage class"""
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """Class serializes instances to JSON file and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary of objects"""
        return FileStorage.__objects

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
        """Deserializes objects from a JSON file"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                objects_dict = json.load(file)
                for key, value in objects_dict.items():
                    class_name, obj_id = key.split(".")
                    obj = BaseModel(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
