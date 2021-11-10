#!/usr/bin/python3
"""
    Test BaseModel module.
"""

import os
from models.base_model import BaseModel
from datetime import datetime
import time
import unittest

from tests.test_models.test_common import TestCommon


class TestBaseModel(TestCommon):
    """
        Test base_model.
    """

    @classmethod
    def setUpClass(self, className=BaseModel):
        """
            Prepare base model tests.
        """

        super().files.append('models/base_model.py')
        super().files.append('tests/test_models/test_base_model.py')
        super().setUpClass(className)

    def test_constructor(self, kwargs={}):
        """
            Test base model initialization.
        """

        obj = self.class_name(**kwargs)
        self.assertIs(type(obj), self.class_name)

    def test_datetime_init(self, kwargs={}):
        """
            Test datetime attribute initialization.
        """

        prev = None

        for index in range(2):
            tic = datetime.utcnow()
            obj = self.class_name(**kwargs)
            toc = datetime.utcnow()

            self.assertTrue(tic <= obj.created_at)
            self.assertTrue(obj.created_at <= toc)
            self.assertEqual(
                obj.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                obj.updated_at.strftime('%Y-%m-%d %H:%M:%S')
            )
            if prev is not None:
                self.assertNotEqual(prev.created_at, obj.created_at)
                self.assertLess(prev.created_at, obj.created_at)
                self.assertNotEqual(prev.updated_at, obj.updated_at)
                self.assertLess(prev.updated_at, obj.updated_at)
            prev = obj

    def test_id(self, kwargs={}):
        """
            Test id initialization.
        """

        prev = None

        for index in range(2):
            obj = self.class_name(**kwargs)
            self.assertEqual(type(obj.id), str)
            self.assertRegex(obj.id,
                             '^[0-9a-f]{8}-[0-9a-f]{4}'
                             '-[0-9a-f]{4}-[0-9a-f]{4}'
                             '-[0-9a-f]{12}$')
            if prev is not None:
                self.assertNotEqual(prev.id, obj.id)
            prev = obj

    def test_created_at_init(self, kwargs=None):
        """
            Test created_at init.
        """

        kwargs = {} if kwargs is None else kwargs
        tic = datetime.utcnow()
        strtic = tic.strftime('%Y-%m-%dT%H:%M:%S.%f')
        with self.assertRaises(TypeError) as context:
            kwargs['created_at'] = tic
            obj = self.class_name(**kwargs)
        kwargs['created_at'] = strtic
        obj = self.class_name(**kwargs)
        self.assertNotEqual(obj.created_at, strtic)
        self.assertEqual(obj.created_at, tic)

    def test_updated_at_init(self, kwargs=None):
        """
            Test updated_at init.
        """

        kwargs = {} if kwargs is None else kwargs
        tic = datetime.utcnow()
        strtic = tic.strftime('%Y-%m-%dT%H:%M:%S.%f')
        with self.assertRaises(TypeError) as context:
            kwargs['updated_at'] = tic
            obj = self.class_name(**kwargs)
        kwargs['updated_at'] = strtic
        obj = self.class_name(**kwargs)
        self.assertNotEqual(obj.updated_at, strtic)
        self.assertEqual(obj.updated_at, tic)

    def test_class_attribute_erase(self, kwargs={}):
        """
            Test __class__ attribute passed is not considered.
        """

        kwargs = {} if kwargs is None else kwargs
        kwargs['__class__'] = None
        obj = self.class_name(**kwargs)
        dict = obj.to_dict()
        self.assertNotEqual(dict['__class__'], 'toto')

    def test_str(self, kwargs={}):
        """
            Test that the str method has the correct output.
        """

        kwargs = {} if kwargs is None else kwargs
        obj = self.class_name(**kwargs)
        string = "[{}] ({}) {}".format(
            obj.__class__.__name__, obj.id, obj.__dict__)
        self.assertEqual(string, str(obj))

    def test_to_dict(self, kwargs={}):
        """
            Test to_dict() method.
        """

        kwargs = {} if kwargs is None else kwargs
        kwargs['name'] = None
        obj = self.class_name(**kwargs)
        expected_attrs = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
        }

        for attribute_name, attribute_type in expected_attrs.items():
            self.assertIn(attribute_name, obj.to_dict().keys())
            self.assertIs(type(obj.__dict__[attribute_name]), attribute_type)
        self.assertNotIn('name', obj.to_dict().keys())
