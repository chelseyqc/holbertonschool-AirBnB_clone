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
        """Test - the all method"""
        self.storage._FileStorage__objects = {
            "Object1": {"id": 1, "name": "Object1"}
        }
        expected = {
            "Object1": {"id": 1, "name": "Object1"}
        }
        self.assertEqual(self.storage.all(), expected)

    def test_filestorage_new(self):
        """Test - the new method creates an object"""
        store = FileStorage()
        base = BaseModel()
        store.new(base)
        key = "{}.{}".format(base.__class__.__name__, base.id)
        self.assertEqual(store._FileStorage__objects[key], base)

    def test_filestorage_save(self):
        """Test - save method saves to file"""
        base = BaseModel()
        base.value = 10
        old = base.updated_at.isoformat()
        base.save()
        new = base.updated_at.isoformat()
        self.assertEqual(base.value, 10)


if __name__ == '__main__':
    unittest.main()
