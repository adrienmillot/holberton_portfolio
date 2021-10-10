#!/usr/bin/python3
"""
    module proposal.
"""
from models.base_model import BaseModel


class Proposal(BaseModel):
    """
        Proposal Model Class.
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
