#!/usr/bin/python3
"""a class City that inherits from BaseModel"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """City unittests"""
    def test_city_state_id(self):
        """Test - City state_id exists"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")

    def test_city_name(self):
        """Test - City name exists"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")

if __name__ == '__main__':
    unittest.main()