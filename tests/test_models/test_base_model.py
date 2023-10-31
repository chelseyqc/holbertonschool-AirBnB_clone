#!/usr/python3
"""BaseModel unit tests"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """BaseModel unit tests"""

    def test_save(self):
        """Test - save method"""
        old_save = str(BaseModel().updated_at)
        BaseModel().save()
        new_save = str(BaseModel().updated_at)
        self.assertNotEqual(old_save, new_save)

    def test_id(self):
        """Test - generates a UUID with no input"""
        base = BaseModel()
        x = base.id != None
        self.assertEqual(x, True)

    def test_to_dict(self):
        """Test - to_dict method"""
        new_dict = BaseModel.__dict__.copy()
        self.assertEqual(new_dict, BaseModel.__dict__)

    def test_str(self):
        """Test - __str__ method"""
        base = BaseModel()
        self.assertEqual(base.__str__(), "[BaseModel] ({}) {}".format(base.id, base.__dict__))

if __name__ == '__main__':
    unittest.main()
