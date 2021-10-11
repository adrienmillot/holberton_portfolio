#!/usr/bin/python3
"""
    Base model module.
"""


from datetime import datetime
from os import getenv
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

if getenv('SS_SERVER_MODE') == "API":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """
        Base model class.
    """

    if getenv('SS_SERVER_MODE') == "API":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)
    else:
        id = None
        created_at = None
        updated_at = None

    def __init__(self, *args, **kwargs):
        """
            Constructor.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

        if 'updated_at' in kwargs:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
        if 'created_at' in kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')

        if '__class__' in kwargs:
            del kwargs['__class__']
        self.__dict__.update(kwargs)

    def __str__(self):
        """
            Return a string repr of BaseModel class.
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def to_dict(self):
        """
            Returns a dictionary containing all keys/values of __dict__
            of the instance.
        """
        new_dict = {}
        new_dict["__class__"] = self.__class__.__name__

        for key, value in self.__dict__.items():
            if not value:
                continue
            if key == "created_at" or key == "updated_at":
                new_dict[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                new_dict[key] = value
        return new_dict
