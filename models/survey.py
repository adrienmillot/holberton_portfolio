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
        return self.__name

    @name.setter
    def name(self, value: str):
        if type(value) is not str:
            raise TypeError()

        self.__name = value
