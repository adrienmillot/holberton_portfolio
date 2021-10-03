#!/usr/bin/python3
"""
    module question.
"""
from models.base_model import BaseModel


class Question(BaseModel):
    """
        Question Model Class.
    """
    __label = ''

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, value: str):
        if type(value) is not str:
            raise TypeError()

        self.__label = value
