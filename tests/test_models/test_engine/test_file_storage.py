""" Defines test cases for Filestorage class """

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorageClass(unittest.TestCase):
    """some of the test cases for FileStorage class """

    def test_all_returns_dict(self):
        """ Test if the all() method returns a dictionary """
        storage = FileStorage()
        obj_dict = storage.all()
        self.assertIsInstance(obj_dict, dict)
        self.assertIs(obj_dict, storage._FileStorage__objects)

    def test_new_method(self):
        """
           Test if the new() method adds an object to
           the __objects dictionary with the correct key
        """
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, storage._FileStorage__objects.keys())
        self.assertIs(storage._FileStorage__objects[key], obj)

    def test_private_class_instance(self):
        """
           Test if the __file_path and __objects attributes are
           initialized whenever a new instance of FileStorage is created
        """
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path, "file.json")
