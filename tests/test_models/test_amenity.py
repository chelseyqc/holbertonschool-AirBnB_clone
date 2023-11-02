#!/usr/bin/python3
"""a class Amenity unittests"""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Amenity unittest"""
    def test_amenity_name(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
