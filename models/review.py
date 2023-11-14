#!/usr/bin/python3
"""Defines a class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a class Review

    Attributes:
        place_id (str): the id of the place
        user_id (str): the user's id
        text (str): text from the user review
    """

    place_id = ""
    user_id = ""
    text = ""
