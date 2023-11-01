#!/usr/bin/python3
"""Unittests for File Storage Class
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime

class TestBase(unittest.TestCase):
    """Test functions for FileStorage Class
    """
    def test_file_path(self):
        """Tests file_path exists
        """
        fs = FileStorage()
        x = fs.file_path is not None
        self.assertEqual(x, True)

    def test_objects(self):
        """Tests objects exists
        """
        fs = FileStorage()
        bm = BaseModel()
        fs.new(bm)
        x = len(fs.objects) > 0
        self.assertEqual(x, True)

        key = "BaseModel." + str(bm.id)
        d = fs.objects[key].to_dict()
        self.assertEqual(bm.id, d["id"])

    def test_all_method_return_type(self):
        """Tests all method return dict
        """
        fs = FileStorage()
        x = len(fs.all()) > 0
        self.assertEqual(x, True)

    def test_save_method_works(self):
        """Tests that save method writes to file successfully
        """
        bm = BaseModel()
        bm.value = 999
        old = bm.updated_at.isoformat()
        bm.save()
        new = bm.updated_at.isoformat()

        self.assertEqual(bm.value, 999)
        self.assertNotEqual(old, new)
