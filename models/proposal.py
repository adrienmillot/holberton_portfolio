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
        label = ''

    def __init__(self, *args, **kwargs):
        """
            Constructor
        """

        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """
            Check attributes.
        """
        if name == 'label' and not isinstance(value, str):
                raise TypeError
        super().__setattr__(name, value)
