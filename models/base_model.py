#!/usr/bin/python3
"""This modul contains tha Base model class"""
import uuid
from datetime import datetime
import json
import models

class BaseModel():
    """Base Model class"""

    def __init__(self, *args, **kwargs):
        """ init method """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        val = datetime.strptime(val, time_format)
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            x = models.storage.new(self)

    def save(self):
        """saving public instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """Ptinting class name, id and dict"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def to_dict(self):
        """Adding to dictionary"""
        new_dict = self.__dict__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
