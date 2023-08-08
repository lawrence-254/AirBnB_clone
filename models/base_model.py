#!/usr/bin/python3
"""class that defines all common attributes/methods for other classes"""

import uuid
from datetime import datetime


class BaseModel():
    """Defining public instance attributes"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    """used to print info"""
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    """Public instance methods
    starting with save
    """
    def save(self):
        self.updated_at = datetime.now()

    """returns a dictionary"""
    def to_dict(self):
        """make temp copy of dict"""
        temp_dict = self.__dict__.copy()

        """add key"""
        temp_dict["__class__"] = self.__class__.__name__
        temp_dict["created_at"] = self.created_at.isoformat()
        temp_dict["updated_at"] = self.updated_at.isoformat()
        return temp_dict
