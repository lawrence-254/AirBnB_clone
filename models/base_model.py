#!/usr/bin/python3
"""class that defines all common attributes/methods for other classes"""

import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage


class BaseModel():
    """Defining public instance attributes"""
    def __init__(self, *args, **kwargs):

        """check if kwargs is empty or not"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            """fule storage"""
            storage.new(self)

    """used to print info"""
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    """Public instance methods
    starting with save
    """
    def save(self):
        self.updated_at = datetime.now()
        """file sorage"""
        storage.save()

    """returns a dictionary"""
    def to_dict(self):
        """make temp copy of dict"""
        temp_dict = self.__dict__.copy()

        """add key"""
        temp_dict["__class__"] = self.__class__.__name__
        temp_dict["created_at"] = self.created_at.isoformat()
        temp_dict["updated_at"] = self.updated_at.isoformat()
        return temp_dict
