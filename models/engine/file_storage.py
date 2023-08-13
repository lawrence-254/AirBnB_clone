#!/usr/bin/python3
"""
serializes instances JSON file and deserializes JSON to instance
"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """
    new class file storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns all class objects
        """
        return self.__objects

    def new(self, obj):
        """
        adds key and value par to our object
        Args:
            obj: the object in question
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serialises and saves our object as JSON
        """
        dict_serial = {}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            for key, val in self.__objects.items():
                dict_serial[key] = val.to_dict()
            json.dump(dict_serial, f)

    def reload(self):
        """Deserializes a JSON string into a dictionary of objects"""
        try:
            path = self.__file_path
            with open(path, mode="r", encoding="utf-8") as file_obj:
                data_strm = json.load(file_obj)
                for key, val in data_strm.items():
                    class_name = key.split(".")[0]
                    self.new(eval(class_name + "(**val)"))
        except FileNotFoundError:
            pass
