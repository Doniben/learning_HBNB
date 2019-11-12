#!/usr/bin/python3
""" File to serialize and deserialize JSON """
import json
from models.base_model import BaseModel
import os

class FileStorage:
    """
    Class that serialize instances to a JSON file
    and deserializes JSON files to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ All objects """
        return self.__objects

    def new(self, obj):
        """ new object """
        key_obj = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key_obj] = obj

    def save(self):
        """ Serialize Json file """
        dict_to_json = {}
        for keys, in self.__objects:
            dict_to_json[keys] = self.__objects[keys].to_dict()
        print (dict_to_json)
        with open(self.__file_path, "w") as file:
            file.write(json.dumps(dict_to_json)

    def reload(self):
        """ Deserialize JSON file """
        new_dict = {"BaseModel": BaseModel}
        """ Dictionary to able the reload """
        if os.path.isfile(self.__file_path)
            with open(self.__file_path, "r") as readed:
                new_data = json.loads(readed.read())
                for key values in new_data.items():
                       self.__objects[key] = new_data[value["__class__"]]
                       (**values)
