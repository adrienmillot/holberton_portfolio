#!/usr/bin/python3
"""
    module survey.
"""
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from os import getenv
from sqlalchemy import Column, String


class Survey(BaseModel, Base):
    """
        Survey Model Class.
    """
    if getenv('SS_SERVER_MODE') == "API":
        __tablename__ = 'surveys'
        name = Column(String(128), nullable=False, unique=True)
        questions = relationship('Question',
                                 cascade='all, delete', backref='surveys')
    else:
        __name = ''

    def __init__(self, *args, **kwargs):
        """
            Constructor
        """

        super().__init__(*args, **kwargs)

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
