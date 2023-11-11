#!/usr/bin/python3
"""Defines the class Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a Place

    Attributes:
        city_id (str): the city id
        user_id (str): the user id.
        name (str): the name of the place.
        description (str): description of the place.
        number_rooms (int): the number of rooms in the place.
        number_bathrooms (int): the number of bathrooms in the place.
        max_guest (int): the max number of guests in the place.
        price_by_night (int): the price by night in the place.
        latitude (float): latitude of the place.
        longitude (float): longitude of the place.
        amenity_ids (list): list of Amenity id's.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
