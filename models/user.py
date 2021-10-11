#!/usr/bin/python3
"""
    module user.
"""
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from models.base_model import Base, BaseModel
from os import getenv
from sqlalchemy import Column, String, DateTime

from models.profile import Profile


answer = Table('answers', Base.metadata,
               Column('proposal_id',
                      String(60),
                      ForeignKey('proposals.id',
                                 onupdate='CASCADE',
                                 ondelete='CASCADE'),
                      primary_key=True),
               Column('user_id', String(60),
                      ForeignKey('users.id',
                                 onupdate='CASCADE',
                                 ondelete='CASCADE'),
                      primary_key=True),
               Column('created_at',
                      DateTime,
                      default=datetime.utcnow),
               Column('updated_at',
                      DateTime,
                      default=datetime.utcnow))


class User(BaseModel, Base):
    """
        User Model Class.
    """
    if getenv('SS_SERVER_MODE') == "API":
        __tablename__ = 'users'
        username = Column(String(128), nullable=False, unique=True)
        password = Column(String(128), nullable=False)
        profile_id = Column(String(60),
                            ForeignKey('profiles.id'), nullable=False)
        answers = relationship("Proposal",
                               secondary=answer,
                               backref="users",
                               viewonly=False)
    else:
        __password = ''
        __username = ''

    def __init__(self, *args, **kwargs):
        """
            Constructor.
        """
        if 'username' not in kwargs:
            raise ValueError('Missing username')
        if 'password' not in kwargs:
            raise ValueError('Missing password')
        if 'profile_id' not in kwargs:
            raise ValueError('Missing profile_id')
        super().__init__(*args, **kwargs)

    @property
    def password(self) -> str:
        """
            Password setter method.
        """
        return self.__password

    @password.setter
    def password(self, value: str):
        """
            Password getter method.
        """

        if type(value) is not str:
            raise TypeError()

        self.__password = value

    @property
    def username(self) -> str:
        """
            Username setter method.
        """

        return self.__username

    @username.setter
    def username(self, value: str):
        """
            Username getter method.
        """

        if type(value) is not str:
            raise TypeError()

        self.__username = value
