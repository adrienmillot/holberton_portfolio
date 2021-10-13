#!/usr/bin/python3
"""
    module user.
"""
from datetime import datetime, timedelta
from hashlib import md5
import hashlib
from typing import Any
import bcrypt
import jwt
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table

from models.profile import Profile

if getenv('SS_SERVER_MODE') == 'API':
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
        password = ''
        username = ''

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

    def encode_auth_token(self, user_id):
        """
            Generates the Auth Token
            :return: string
        """
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(days=0, seconds=43200),
                'iat': datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                getenv('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
            Decodes the auth token
            :param auth_token:
            :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, getenv('SECRET_KEY'))

            return payload['sub']
        except jwt.ExpiredSignatureError:
            return -2
        except jwt.InvalidTokenError:
            return -1

    def encode_bcrypt(self, string: str) -> str:
        """
            Encode a string with md5
        """

        salt = bcrypt.gensalt()

        return bcrypt.hashpw(
            string.encode('utf-8'), salt
        )

    def __setattr__(self, name, value):
        """
            Check attributes.
        """

        if name == 'username' and type(value) is not str:
            raise TypeError

        if name == 'password':
            if type(value) is not str:
                raise TypeError

            if (
                not hasattr(self, 'password') or
                value != getattr(self, 'password')
            ):
                value = self.encode_bcrypt(value)

        super(User, self).__setattr__(name, value)
