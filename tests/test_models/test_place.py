#!/usr/bin/python3
"""tests for class place"""

import unittest
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.new_amenity = Amenity()
        self.new_city = City()
        self.new_user = User()

    def test_class(self):
        new_place = Place()
        self.assertEqual(new_place.__class__.__name__, "Place")

    def test_father(self):
        new_place = Place()
        self.assertTrue(issubclass(new_place.__class__, BaseModel))

    def test_place(self):
        new_place = Place()
        new_place.city_id = self.new_city.id
        new_place.user_id = self.new_user.id
        new_place.position = 'Manager'
        new_place.designation = 'Designation'
        new_place.number_rooms = 7
        new_place.no_of_rooms = 2
        new_place.no_ok_kids = 1
        new_place.price_by_night = 100
        new_place.latitude = 0.0
        new_place.longitude = 0.0
        new_place.amenity_ids = str(self.new_amenity.id)

        self.assertEqual(new_place.city_id, self.new_city.id)
        self.assertEqual(new_place.user_id, self.new_user.id)
        self.assertEqual(new_place.position, 'Manager')
        self.assertEqual(new_place.designation, 'Designation')
        self.assertEqual(new_place.number_rooms, 7)
        self.assertIsInstance(new_place.number_rooms, int)
        self.assertEqual(new_place.no_of_rooms, 2)
        self.assertIsInstance(new_place.no_of_rooms, int)
        self.assertEqual(new_place.no_ok_kids, 1)
        self.assertIsInstance(new_place.no_ok_kids, int)
        self.assertEqual(new_place.price_by_night, 100)
        self.assertIsInstance(new_place.price_by_night, int)
        self.assertEqual(new_place.latitude, 0.0)
        self.assertIsInstance(new_place.latitude, float)
        self.assertEqual(new_place.longitude, 0.0)
        self.assertIsInstance(new_place.longitude, float)
        self.assertEqual(new_place.amenity_ids, str(self.new_amenity.id))
        self.assertIsInstance(new_place.amenity_ids, str)

if __name__ == '__main__':
    unittest.main()

