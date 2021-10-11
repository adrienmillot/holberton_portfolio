#!/usr/bin/python3
"""
    Database Storage Module for API Server Mode.
"""


from models.base_model import Base
from models.engine.common_storage import CommonStorage
from models.category import Category
from models.profile import Profile
from models.proposal import Proposal
from models.question import Question
from models.survey import Survey
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker, scoped_session
import os


@CommonStorage.register
class DBStorage(CommonStorage):
    """
        Class that manages Database Storage.
    """

    __engine = None
    __session = None

    classes = {"Category": Category, "Profile": Profile,
               "Proposal": Proposal, "Question": Question, "Survey": Survey,
               "User": User}

    def __init__(self) -> None:
        """
            Retrieve environment variables and initialize engine.
        """

        mysql_user = os.environ.get('SS_MYSQL_USER')
        mysql_pwd = os.environ.get('SS_MYSQL_PWD')
        db_host = os.environ.get('SS_MYSQL_HOST')
        db = os.environ.get('SS_MYSQL_DB')
        env = os.environ.get('SS_SERVER_ENVIRONMENT')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}?use_unicode=1&charset=utf8'.format(
                mysql_user,
                mysql_pwd,
                db_host,
                db,
            ), pool_pre_ping=True
        )

        if env == 'test' and db == 'ss_test_db':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
            Return a dictionary representation of all objects
            from a class present in the database (or all class
            if not specified).
        """
        new_dict = {}
        for class_name, class_value in self.classes.items():
            if cls is None or cls is class_value or cls is class_name:
                objs = self.__session.query(class_value).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def close(self):
        """
            Call reload() method for deserializing the JSON file to objects.
        """

        self.__session.close()

    def count(self, cls=None):
        """
            Count the number of objects in storage.
        """

        return len(self.all(cls))

    def delete(self, obj=None):
        """
            Delete obj from __objects if it’s inside.
        """

        if obj is not None:
            self.__session.delete(obj)

    def get(self, cls, id):
        """
            Returns the object based on the class name and its ID, or
            None if not found.
        """

        query = self.__session.query(cls)
        if id is None:
            return None
        return query.get(id)

    def new(self, obj):
        """
            Adds a new object to the database.
        """

        self.__session.add(obj)

    def reload(self):
        """
            Reloads data from the database.
        """

        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        session_class = scoped_session(sess_factory)
        self.__session = session_class

    def save(self):
        """
            Save all changes to the database.
        """

        self.__session.commit()
