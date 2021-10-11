#!/usr/bin/python3
"""
    module profile.
"""
from datetime import datetime
from os import getenv
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
    else:
        __last_name = ''
        __first_name = ''
        __gender = ''
        __born_at = None

    def __init__(self, *args, **kwargs):
        """
            Constructor.
        """

        if 'born_at' in kwargs:
            kwargs['born_at'] = datetime.strptime(kwargs['born_at'],
                                                  '%Y-%m-%dT%H:%M:%S.%f')
            self.born_at = kwargs['born_at']
        super().__init__(*args, **kwargs)

    @property
    def last_name(self) -> str:
        """
            Last name setter method.
        """

        return self.__last_name

    @last_name.setter
    def last_name(self, value: str):
        """
            Last name getter method.
        """

        if type(value) is not str:
            raise TypeError()

        self.__last_name = value

    @property
    def first_name(self) -> str:
        """
            First name setter method.
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        """
            First name getter method.
        """

        if type(value) is not str:
            raise TypeError()

        self.__first_name = value

    @property
    def gender(self) -> str:
        """
            Gender setter method.
        """

        return self.__gender

    @gender.setter
    def gender(self, value: str):
        """
            Gender getter method.
        """

        if type(value) is not str:
            raise TypeError()

        if value.capitalize() not in ['Male', 'Female', 'Trans', 'Queer']:
            raise ValueError('Invalid gender')

        self.__gender = value.capitalize()

    @property
    def born_at(self) -> datetime:
        """
            Born at setter method.
        """

        return self.__born_at

    @born_at.setter
    def born_at(self, value: datetime):
        """
            Born at getter method.
        """

        if type(value) is not datetime:
            raise TypeError()

        now = datetime.utcnow()

        if now.year - value.year < 18:
            raise ValueError('Not major')

        self.__born_at = value
