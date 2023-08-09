#!/usr/bin/python3
"""serializes instances JSON file and deserializes JSON to instance"""

from models.base_model import BaseModel
import json


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{self.__class__.__name__}.{self.id}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, "w", encoding="utf-8") as fil:
            dic = {k : v.to_dict() for k, v in self.__objects.items()}
            json.dump(dic, fil)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="utf-8" ) as fil:
                obj_dict = json.load(fil)
                obj_dict = eval(self.__class__.__name__(obj_dict))
        except FileNotFoundError:
            pass
