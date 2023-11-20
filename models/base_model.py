#!/usr/bin/python3
"""Script defines a class BaseModel"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Represent base class for HBnB project"""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        Args:
            *args (any): non-keyword arguments
            **kwargs (dict): key and value pairs of attributes
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    class_name = value
                    if class_name in models.storage.classes:
                        self.__class__ = models.storage.classes[class_name]
                    elif key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update 'updated_at' attribute with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dict representation of BaseModel instance"""
        ob_dict = self.__dict__.copy()
        ob_dict["__class__"] = self.__class__.__name__
        ob_dict["created_at"] = self.created_at.isoformat()
        ob_dict["updated_at"] = self.updated_at.isoformat()
        return ob_dict
