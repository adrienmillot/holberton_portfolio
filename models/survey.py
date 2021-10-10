#!/usr/bin/python3
"""
    module survey.
"""
from models.base_model import BaseModel


class Survey(BaseModel):
    """
        Survey Model Class.
    """
    __name = ''

    @property
    def name(self) -> str:
        """
            Name setter method.
        """

        return self.__name

    @name.setter
    def name(self, value: str):
        """
            Name getter method.
        """

        if type(value) is not str:
            raise TypeError()

        self.__name = value
