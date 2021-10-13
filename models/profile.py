#!/usr/bin/python3
"""
    module profile.
"""
from datetime import datetime
from os import getenv

from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, DateTime


class Profile(BaseModel, Base):
    """
        Profile Model Class.
    """

    if getenv('SS_SERVER_MODE') == "API":
        __tablename__ = 'profiles'
        last_name = Column(String(128), nullable=True)
        first_name = Column(String(128), nullable=True)
        gender = Column(String(6), nullable=True)
        born_at = Column(DateTime, nullable=True)
        user = relationship('User', cascade='all, delete', backref='profiles')
    else:
        last_name = ''
        first_name = ''
        gender = ''
        born_at = None

    def __init__(self, *args, **kwargs):
        """
            Constructor.
        """

        if 'born_at' in kwargs:
            kwargs['born_at'] = datetime.strptime(kwargs['born_at'],
                                                  '%Y-%m-%dT%H:%M:%S.%f')
            self.born_at = kwargs['born_at']
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """
            Check attributes.
        """
        if name == 'last_name' and not isinstance(value, str):
                raise TypeError

        if name == 'first_name' and not isinstance(value, str):
                raise TypeError

        if name == "born_at":

            if type(value) is not datetime:
                raise TypeError()

            now = datetime.utcnow()

            if now.year - value.year < 18:
                raise ValueError('Not major')

        if name == 'gender':

            if type(value) is not str:
                raise TypeError()

            if value.capitalize() not in ['Male', 'Female', 'Trans', 'Queer']:
                raise ValueError('Invalid gender')

            value = value.capitalize()

        super().__setattr__(name, value)
