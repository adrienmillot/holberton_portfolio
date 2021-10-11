#!/usr/bin/python3
"""
    module user.
"""
from models.base_model import Base, BaseModel
from os import getenv
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """
        User Model Class.
    """
    if getenv('SS_SERVER_MODE') == "API":
        __tablename__ = 'users'
        username = Column(String(128), nullable=False, unique=True)
        password = Column(String(128), nullable=False)
    else:
        __password = ''
        __username = ''

    def __init__(self, *args, **kwargs):
        """
            Constructor.
        """
        if 'username' not in kwargs:
            raise ValueError('Missing username')
        if 'password' not in kwargs:
            raise ValueError('Missing password')
        super().__init__(*args, **kwargs)

    @property
    def password(self) -> str:
        """
            Password setter method.
        """
        return self.__password

    @password.setter
    def password(self, value: str):
        """
            Password getter method.
        """

        if type(value) is not str:
            raise TypeError()

        self.__password = value

    @property
    def username(self) -> str:
        """
            Username setter method.
        """

        return self.__username

    @username.setter
    def username(self, value: str):
        """
            Username getter method.
        """

        if type(value) is not str:
            raise TypeError()

        self.__username = value
