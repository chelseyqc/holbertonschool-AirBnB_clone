#!/usr/bin/python3
"""class User unittests"""
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Test - the User class has an email"""
    def test_user_email_exists(self):
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def test_user_password(self):
        """Test - the User class has a password"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def test_user_first_name(self):
        """Test - the User class has a first_name"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")

    def test_user_last_name(self):
        """Test - the User has a last_name"""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")
