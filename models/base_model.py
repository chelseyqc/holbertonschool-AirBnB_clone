#!/usr/python3
"""BaseModel module"""
import json
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """instantiation of class attributes"""
        if len(kwargs) != 0:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, date_format)
                    setattr(self, key, value)
                else:
                    if key != '__class__':
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """prints the string specified"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at to current"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = type(self).__name__
        return new_dict

    def remove(self):
        """Removes current instance reference from within objects
        and saves it"""
        key = self.__class__.__name__ + "." + self.id
        obj = storage.objects
        obj.pop(key)
        storage.objects = obj
        storage.save()
