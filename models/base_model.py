#!/usr/bin/python3
"""This modul contains tha Base model class"""
import models
import uuid
import datetime

class BaseModel():
    """Base Model class"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.create_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        """saving"""
        self.update_at = datetime.datetime.now()

    def __str__(self):
        """Ptinting class name, id and dict"""
        return "[BaseModel] %s %s" %(self.id, self.__dict__)

    def to_dict(self):
        """Adding to dictionary"""
        new_dict = self.__dict__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        new_dict[__class__] = type(self).__name__
        return new_dict
