#!/usr/bin/python3
"""class State unittests"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """State unittests"""
    def test_state_name(self):
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

if __name__ == '__main__':
    unittest.main()