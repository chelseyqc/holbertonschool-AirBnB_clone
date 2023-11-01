#!/usr/bin/python3
"""class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class

    Attributes:
        email (str): an empty string
        password (str): an empty string
        first_name (str): an empty string
        last_name (str): an empty
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
