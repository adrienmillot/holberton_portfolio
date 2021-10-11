#!/usr/bin/python3
"""
    module proposal.
"""
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from os import getenv


class Proposal(BaseModel, Base):
    """
        Proposal Model Class.
    """
    if getenv('SS_SERVER_MODE') == "API":
        __tablename__ = 'proposals'
        label = Column(String(256), nullable=False)
        question_id = Column(String(60),
                             ForeignKey('questions.id'), nullable=False)
        is_valid = Column(Boolean, nullable=True, default=False)
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
