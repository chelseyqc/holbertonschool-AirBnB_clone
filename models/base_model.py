#!/usr/python3
"""BaseModel module"""
import json
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class"""

    def __init__(self):
        """instantiation of class attributes"""
        self.id = uuid.uuid4()
        current_create = datetime.now()
        self.created_at = current_create.strftime('%Y-%m-%dT%H:%M:%S.%f')
        current_update = datetime.now()
        self.updated_at = current_update.strftime('%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """prints the string specified"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at to current"""
        current_time = datetime.now()
        self.updated_at = current_time.strftime('%Y-%m-%dT%H:%M:%S.%f')

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        return new_dict
