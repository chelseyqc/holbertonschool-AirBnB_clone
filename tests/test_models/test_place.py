#!/usr/bin/python3
"""class Place unittests"""
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Place unittests"""

    def test_place_city_id(self):
        """Test - city_id exists"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")

    def test_place_user_id(self):
        """Test - user_id exists"""
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")

    def test_place_name(self):
        """Test - name exists"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")

    def test_place_description(self):
        """Test - description exists"""
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")

    def test_place_number_rooms(self):
        """Test - number_rooms exists"""
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(place.number_rooms, 0)

    def test_place_number_bathrooms(self):
        """Test - number_bathrooms exists"""
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(place.max_guest, 0)

    def test_place_price_by_night(self):
        """Test - price_by_night exists"""
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(place.price_by_night, 0)

    def test_place_latitude(self):
        """Test - latitude exists"""
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(place.latitude, 0.0)

    def test_place_longitude(self):
        """Test - longitude exists"""
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(place.longitude, 0.0)

    def test_place_amenity_ids(self):
        """Test - longitude exists"""
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(place.amenity_ids, [])
