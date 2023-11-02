#!/usr/bin/python3
"""BaseModel unit tests"""
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """BaseModel unit tests"""

    def test_save(self):
        """Test - save method"""
        base = BaseModel()
        new_save = base.updated_at
        base.save()
        selfassertLess(new_save, base.updated_at)
        self.assertLess(new_save, base.updated_at)
        self.assertTrue(os.path.exists("file.json"))

    def test_id(self):
        """Test - generates a UUID with no input"""
        base = BaseModel()
        x = base.id != None
        self.assertEqual(x, True)

    def test_to_dict(self):
        """Test - to_dict method"""
        base = BaseModel()
        new_dict = base.to_dict()
        self.assertEqual(base.id, new_dict["id"])

    def test_str(self):
        """Test - __str__ method"""
        base = BaseModel()
        self.assertEqual(base.__str__(), "[BaseModel] ({}) {}".format(base.id, base.__dict__))

if __name__ == '__main__':
    unittest.main()
