#!/usr/bin/python3
"""File Storage tests"""
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """FileStorage unit tests"""

    def setUp(self):
        """Sets up the class"""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up crew"""
        self.storage = None

    def test_filestorage_file_path(self):
        """Test - that there is a file path"""
        path = self.storage._FileStorage__file_path
        self.assertEqual(path, "file.json")

    def test_filestorage_objects(self):
        """Test - that objects exists"""
        store = FileStorage()
        base = BaseModel()
        key = "{}.{}".format(base.__class__.__name__, base.id)
        obj1 = self.storage._FileStorage__objects
        self.assertEqual(obj1[key], base)

    def test_filestorage_all(self):
        """Test - the all method returns an empty dictionary"""
        store = FileStorage()
        result = store.all()
        self.assertEqual(result, store._FileStorage__objects)

    def test_filestorage_new(self):
        """Test - the new method creates an object"""
        store = FileStorage()
        base = BaseModel()
        store.new(base)
        key = "{}.{}".format(base.__class__.__name__, base.id)
        self.assertEqual(store._FileStorage__objects[key], base)

if __name__ == '__main__':
    unittest.main()
