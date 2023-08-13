#!/usr/bin/python3
'''test cases for class reviews'''
import unittest
from models.place import Place
from models.review import Review
from models.user import User


class TestReview(unittest.TestCase):

    def setUp(self):
        self.new_place = Place()
        self.new_user = User()

    def test_class_name(self):
        my_review = Review()
        self.assertEqual(my_review.__class__.__name__, "Review")

    def test_inheritance(self):
        my_review = Review()
        self.assertTrue(issubclass(my_review.__class__, BaseModel))

    def test_review_attributes(self):
        """
        Test cases for attributes of Class Review
        """
        my_review = Review()
        my_review.place_id = self.new_place.id
        my_review.user_id = self.new_user.id
        my_review.text = 'holberton'

        self.assertEqual(my_review.place_id, self.new_place.id)
        self.assertEqual(my_review.user_id, self.new_user.id)
        self.assertEqual(my_review.text, 'holberton')


if __name__ == '__main__':
    unittest.main()
