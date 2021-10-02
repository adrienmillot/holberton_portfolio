#!/usr/bin/python3
"""
    Test BaseModel module.
"""

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

    def test_constructor(self):
        """
            Test base model initialization.
        """
        obj = self.className()
        self.assertIs(type(obj), self.className)

    def test_datetime_init(self):
        """
            Test datetime attribute initialization.
        """
        obj_list = []
        prev = None

        for index in range(2):
            tic = datetime.utcnow()
            obj = self.className()
            toc = datetime.utcnow()

            self.assertTrue(tic <= obj.created_at)
            self.assertTrue(obj.created_at <= toc)
            self.assertEqual(obj.created_at, obj.updated_at)
            if prev is not None:
                self.assertNotEqual(prev.created_at, obj.created_at)
                self.assertLess(prev.created_at, obj.created_at)
                self.assertNotEqual(prev.updated_at, obj.updated_at)
                self.assertLess(prev.updated_at, obj.updated_at)
            prev = obj

    def test_id(self):
        """
            Test id initialization.
        """

        obj_list = []
        prev = None

        for index in range(2):
            obj = self.className()
            self.assertEqual(type(obj.id), str)
            self.assertRegex(obj.id,
                             '^[0-9a-f]{8}-[0-9a-f]{4}'
                             '-[0-9a-f]{4}-[0-9a-f]{4}'
                             '-[0-9a-f]{12}$')
            if prev is not None:
                self.assertNotEqual(prev.id, obj.id)
            prev = obj

    def test_to_dict(self):
        """
            Test to_dict() method.
        """

        obj = self.className(name=None)
        expected_attrs = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
        }

        for attribute_name, attribute_type in expected_attrs.items():
            self.assertIn(attribute_name, obj.to_dict().keys())
            self.assertIs(type(obj.__dict__[attribute_name]), attribute_type)
        self.assertNotIn('name', obj.to_dict().keys())
