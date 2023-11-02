#!/usr/bin/python3
"""class Review tests"""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Review unittests"""
    def test_review_place_id(self):
        """Test - place_id exists"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")

    def test_review_user_id(self):
        """Test - user_id exists"""
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")

    def test_review_text(self):
        """Test - text exists"""
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")

if __name__ == '__main__':
    unittest.main()