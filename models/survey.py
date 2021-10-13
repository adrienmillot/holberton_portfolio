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
        name = ''

    def __init__(self, *args, **kwargs):
        """
            Constructor
        """

        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """
            Check attributes.
        """
        if name == 'name' and not isinstance(value, str):
            raise TypeError
        super(Survey, self).__setattr__(name, value)
