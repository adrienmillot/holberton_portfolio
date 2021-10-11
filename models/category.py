#!/usr/bin/python3
"""
    module category.
"""
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import Base, BaseModel
from os import getenv
from sqlalchemy import Column, String


class Category(BaseModel, Base):
    """
        Category Model Class.
    """
    if getenv('SS_SERVER_MODE') == "API":
        __tablename__ = 'categories'
        name = Column(String(128), nullable=False, unique=True)
        questions = relationship('Question',
                                 cascade='all, delete', backref='categories')
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
