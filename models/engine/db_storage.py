#!/usr/bin/python3
"""
    Database Storage Module for API Server Mode.
"""


from datetime import datetime
from sqlalchemy.sql.elements import and_

from sqlalchemy.sql.expression import null
from models import question
from models.base_model import Base
from models.category import Category
from models.profile import Profile
from models.proposal import Proposal
from models.question import Question
from models.survey import Survey
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker, scoped_session
import os


class DBStorage:
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

    def all(self, cls=None, limit=None, page=None):
        """
            Return a dictionary representation of all objects
            from a class present in the database (or all class
            if not specified).
        """
        new_dict = {}
        for class_name, class_value in self.classes.items():
            if cls is None or cls is class_value or cls is class_name:
                query = self.__session.query(class_value)

                if limit is not None :
                    query = query.limit(limit)

                if page is not None and page > 0:
                    query = query.offset((page - 1) * limit)

                objs = query.all()
                for obj in objs:
                    if (
                        hasattr(obj, 'deleted_at') and
                        type(obj.deleted_at) is not datetime
                    ):
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

    def disable(self, obj=None):
        """
            Disable obj from __objects if it’s inside.
        """

        if obj is not None:
            obj.deleted_at = datetime.utcnow()
            self.save()

    def delete(self, obj=None):
        """
            Delete obj from __objects if it’s inside.
        """

        env = os.environ.get('SS_SERVER_ENVIRONMENT')
        db = os.environ.get('SS_MYSQL_DB')

        if (
            env == 'test' and db == 'ss_test_db' and
            obj is not None
        ):
            self.__session.delete(obj)

    def get(self, cls, id):
        """
            Returns the object based on the class name and its ID, or
            None if not found.
        """

        if id is None:
            return None

        query = self.__session.query(cls).filter_by(deleted_at=None, id=id)

        if query.count() == 0:
            return None

        return query.first()

    def get_from_attributes(self, cls, **kwargs):
        """
        """

        query = self.__session.query(cls).filter_by(**kwargs)

        return query.first()

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

    def random_survey_question(self, survey_id, user_id):
        """
            SQL query to retrieve all unanswered questions of
            a surveys for a specified user.
        """

        subquery = self.__session.query(Proposal).with_entities(
            Proposal.question_id).join(User.answers).filter(User.id == user_id).subquery()
        query = self.__session.query(Question).join(Survey.questions).filter(
            Question.id.notin_(subquery), Survey.id == survey_id)

        return (query.count(), query.first())

    def unanswered_survey(self, user_id):
        """
            SQL query to retrieve all unanswered surveys for a
            specified user.
        """

        subquery = self.__session.query(Proposal).with_entities(
            Proposal.question_id).join(User.answers).filter(User.id == user_id).subquery()
        query = self.__session.query(Question).with_entities(Survey).join(
            Survey.questions).filter(Question.id.notin_(subquery))

        return query.all()

    def all_question_proposals(self, question_id):
        """
            SQL query to retrieve all proposal of a specified question.
        """

        query = self.__session.query(Proposal).filter(Proposal.question_id == question_id)

        return query.all()
