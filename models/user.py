#!/usr/bin/python3
"""
    module user.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        User Model Class.
    """
    __password = ''
    __username = ''

    def __init__(self, *args, **kwargs):
        """
            Constructor
        """
        if 'username' not in kwargs:
            raise ValueError('Missing username')
        if 'password' not in kwargs:
            raise ValueError('Missing password')
        super().__init__(*args, **kwargs)

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, value: str):
        if type(value) is not str:
            raise TypeError()

        self.__password = value

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, value: str):
        if type(value) is not str:
            raise TypeError()

        self.__username = value
