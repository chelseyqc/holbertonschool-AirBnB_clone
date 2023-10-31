#!/usr/python3
"""File Storage"""
import json
import sys
import os


class FileStorage:
    """File Storage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        value = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[value] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        empty_dict = {}
        for key in self.__objects:
            empty_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(empty_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects if the JSON file exists"""
        from models.base_model import BaseModel

        reloaded = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                reloaded = json.load(file)
        else:
            pass
        for key, obj in reloaded.items():
            self.__objects[key] = BaseModel(**obj)
