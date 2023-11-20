#!/usr/bin/python3
"""Define a class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent City
    Attributes:
        state_id (str): string to represent the state id
        name (str): string to represent name of city
    """

    state_id = ""
    name = ""
