#!/usr/bin/python3
"""
    module question.
"""
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import Base, BaseModel
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Question(BaseModel, Base):
    """
        Question Model Class.
    """
    if getenv('SS_SERVER_MODE') == "API":
        __tablename__ = 'questions'
        label = Column(String(256), primary_key=True)
        category_id = Column(String(60),
                             ForeignKey('categories.id'), nullable=False)
        survey_id = Column(String(60),
                           ForeignKey('surveys.id'), nullable=False)
        proposals = relationship("Proposal",
                                 cascade="all, delete", backref="questions")

    else:
        __label = ''

    def __init__(self, *args, **kwargs):
        """
            Constructor
        """

        super().__init__(*args, **kwargs)

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
