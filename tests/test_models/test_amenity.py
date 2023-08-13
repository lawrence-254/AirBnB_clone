#!/usr/bin/python3
'''tests cases for class amenity'''

import unittest
from ..models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.new_amenity = Amenity()

    def test_class_name(self):
        self.assertEqual(self.new_amenity.__class__.__name__, "Amenity")

    def test_inheritance(self):
        self.assertTrue(issubclass(self.new_amenity.__class__, BaseModel))

    def test_amenity_attributes(self):
        """Test cases for attributes of Class Amenity"""
        self.new_amenity.name = "Kimber hunting ground"
        self.assertEqual(self.new_amenity.name, 'kimber hunting ground')


if __name__ == '__main__':
    unittest.main()
