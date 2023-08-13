#!/usr/bin/python3
"""test perfomance of stateobject"""


import unittest
from models.base_model import BaseModel
from models.state import State


class Teststate(unittest.TestCase):
    def test_class(self):
        new_state = State()
        self.assertEqual(new_state.__class__.__name__, "State")

    def test_state(self):
        """attributes test"""
        new_state = State()
        new_state.name = "holberton"
        self.assertEqual(new_state.name, 'holberton')
