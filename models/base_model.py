#!/usr/bin/python3
"""
    Base model module.
"""


from datetime import datetime
import json
import models
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
        deleted_at = Column(DateTime, default=None)
    else:
        id = None
        created_at = None
        updated_at = None
        deleted_at = None

    def __init__(self, *args, **kwargs):
        """
            Constructor.
        """

        if kwargs:
            if kwargs.get("created_at", None):
                self.created_at = datetime.strptime(
                    kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f')
                del kwargs["created_at"]
            else:
                self.created_at = datetime.utcnow()

            if kwargs.get("updated_at", None):
                self.updated_at = datetime.strptime(
                    kwargs["updated_at"], '%Y-%m-%dT%H:%M:%S.%f')
                del kwargs["updated_at"]
            else:
                self.updated_at = datetime.utcnow()

            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())

            for key, value in kwargs.items():
                if key != "__class__" and value is not None:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

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
            elif key in ("_sa_instance_state", "password"):
                continue
            else:
                new_dict[key] = value
        return new_dict

    def save(self):
        """
            updates the attribute 'updated_at' with the current datetime
        """

        self.updated_at = datetime.utcnow()

        models.db_storage.new(self)
        models.db_storage.save()

    def delete(self):
        """
            delete the current instance from the storage
        """

        models.db_storage.disable(self)

    def __setattr__(self, name: str, value) -> None:
        """
            Check attributes.
        """

        if (
            name in ('created_at', 'updated_at') and
            not isinstance(value, datetime)
        ):
            raise TypeError

        super(BaseModel, self).__setattr__(name, value)
