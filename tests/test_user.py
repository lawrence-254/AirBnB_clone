#!/usr/bin/python3
"""user object tests"""

import unittest
from models.user import User


class Testuser(unittest.TestCase):
    """class test user to initialize tests"""
    def test_User(self):
        '''test user attributes if are correct'''
        new_user = User()
        new_user.first_name = 'First'
        new_user.last_name = 'Last'
        new_user.email = 'user@mail.com'
        self.assertEqual(new_user.first_name, 'First')
        self.assertEqual(new_user.last_name, 'Last')
        self.assertEqual(new_user.email, 'user@mail.com')
