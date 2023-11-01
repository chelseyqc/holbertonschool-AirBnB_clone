#!/usr/bin/python3
"""a class Review that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review"""
    place_id = ""
    user_id = ""
    text = ""
