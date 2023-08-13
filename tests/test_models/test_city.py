#!/usr/bin/python3
'''test cases for class city'''

import unittest
from models.city import City
from models.state import State


class TestCity(unittest.TestCase):

    def test_class_name(self):
        city = City()
        self.assertEqual(city.__class__.__name__, "City")

    def test_inheritance(self):
        city = City()
        self.assertTrue(issubclass(city.__class__, BaseModel))

    def test_city_attributes(self):
        """
        Test casses attributes for Class City
        """
        new_city = City()
        new_state = State()
        new_city.name = "holberton"
        new_city.state_id = new_state.id
        self.assertEqual(new_city.name, 'holberton')
        self.assertEqual(new_city.state_id, new_state.id)


if __name__ == '__main__':
    unittest.main()
