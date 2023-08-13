#!/usr/bin/python3
"""import base model"""

from models.base_model import BaseModel

"""A puthon class user that inherits from base model class"""


class User(BaseModel):
    """class user that deals with the information of clients"""
    first_name = ""
    last_name = ""
    email = ""
    password = ""
