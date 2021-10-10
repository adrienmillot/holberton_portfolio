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
        """
            Label setter method.
        """

        return self.__label

    @label.setter
    def label(self, value: str):
        """
            Label getter method.
        """

        if type(value) is not str:
            raise TypeError()

        self.__label = value
