#!/usr/bin/python3
"""Defines a class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent a class Amenity

    Attributes:
        name (str): name of the amenity
    """
    
    name = ""
