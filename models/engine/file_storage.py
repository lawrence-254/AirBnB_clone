#!/usr/bin/python3
"""
serializes instances JSON file and deserializes JSON to instance
"""
import json
from models import base_model


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
            FileStorage.__objects.clear()
            with open('file.json', 'r') as f:
                all_obj = json.load(f)
                for key, val in all_obj.items():
                    class_name = val.get("__class__")
                    if class_name is not None:
                        class_type = globals().get(class_name)
                        if class_type is not None:
                            instance = class_type(**val)
                            FileStorage.__objects[key] = instance
                        else:
                            print(f"Class {class_name} not found")
                    else:
                        print(f"No class information found for object with key {key}")
        except FileNotFoundError:
            return
        except json.JSONDecodeError as e:
            print("JSON Decode Error:", e)
