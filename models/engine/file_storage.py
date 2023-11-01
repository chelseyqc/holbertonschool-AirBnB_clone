#!/usr/python3
"""File Storage"""
import json
import sys
import os


class FileStorage:
    """File Storage class"""

    __file_path = "file.json"
    __objects = {}

    @property
    def file_path(self):
        """Gets the file_path"""
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        """Sets the file_path"""
        self.__file_path = value

    @property
    def objects(self):
        """Gets the objects"""
        return self.__objects

    @objects.setter
    def objects(self, value):
        """Sets the objects"""
        self.__objects = value

    def all(self):
        """returns the dictionary __objects"""
        return self.objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        value = obj.__class__.__name__ + "." + str(obj.id)
        self.objects[value] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        empty_dict = {}
        for key in self.objects:
            empty_dict[key] = self.objects[key].to_dict()
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(empty_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects if the JSON file exists"""
        from models.base_model import BaseModel

        reloaded = {}
        if os.path.exists(self.__file_path):
            with open(self.file_path, 'r', encoding="utf-8") as file:
                reloaded = json.load(file)
        else:
            pass
        for key, obj in reloaded.items():
            self.objects[key] = BaseModel(**obj)
