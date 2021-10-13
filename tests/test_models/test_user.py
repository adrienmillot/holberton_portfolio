#!/usr/bin/python3
"""
    Test User Module.
"""
from datetime import datetime
from uuid import uuid4

import bcrypt
from models.user import User
from tests.test_models.test_base_model import TestBaseModel


class TestUser(TestBaseModel):
    """
        Test User Model.
    """

    @classmethod
    def setUpClass(self):
        """
            Set up for docstring tests
        """

        super().files.append('models/user.py')
        super().files.append('tests/test_models/test_user.py')
        super().setUpClass(User)

    def setUp(self) -> None:
        self.kwargs = {
            'username': 'toto',
            'password': 'password',
            'profile_id': uuid4
        }

    def test_constructor(self):
        """
            Test base model initialization.
        """

        return super().test_constructor(kwargs=self.kwargs)

    def test_datetime_init(self):
        """
            Test datetime attribute initialization.
        """

        return super().test_datetime_init(kwargs=self.kwargs)

    def test_id(self):
        """
            Test id initialization.
        """

        return super().test_id(kwargs=self.kwargs)

    def test_any_username(self):
        """
            Test wrong name type insertion.
        """

        with self.assertRaises(ValueError) as context:
            obj = self.class_name()

    def test_username_setter(self):
        """
            Test username setter method.
        """

        obj = self.class_name(**self.kwargs)
        obj.username = "toto"

        self.assertEqual("toto", obj.username)

    def test_wrong_username(self):
        """
            Test wrong name type insertion.
        """

        with self.assertRaises(Exception) as context:
            obj = self.class_name(**self.kwargs)
            obj.username = 12

    def test_any_password(self):
        """
            Test wrong name type insertion.
        """

        with self.assertRaises(ValueError) as context:
            obj = self.class_name(username="toto")

    def test_password_setter(self):
        """
            Test password setter method.
        """

        obj = self.class_name(**self.kwargs)
        obj.password = 'toto'

        self.assertTrue(bcrypt.checkpw('toto'.encode('utf-8'), obj.password))

    def test_wrong_password(self):
        """
            Test wrong name type insertion.
        """

        with self.assertRaises(Exception) as context:
            obj = self.class_name(**self.kwargs)
            obj.password = 12

    def test_to_dict(self):
        """
            Test to_dict() method.
        """

        obj = self.class_name(**self.kwargs)
        super().test_to_dict(kwargs=self.kwargs)
        self.assertIn('username', obj.to_dict().keys())
        self.assertIn('toto', obj.to_dict().values())

    def test_class_attribute_erase(self):
        """
            Test __class__ attribute passed is not considered.
        """

        super().test_class_attribute_erase(kwargs=self.kwargs)

    def test_created_at_init(self):
        """
            Test created_at init.
        """

        return super().test_created_at_init(kwargs=self.kwargs)

    def test_updated_at_init(self):
        """
            Test updated_at init.
        """

        return super().test_updated_at_init(kwargs=self.kwargs)

    def test_str(self):
        """
            Test that the str method has the correct output.
        """

        return super().test_str(kwargs=self.kwargs)
