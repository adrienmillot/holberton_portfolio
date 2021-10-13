#!/usr/bin/python3
"""
    File Storage test Module
"""
from datetime import datetime
import os
from models.category import Category
from models.engine.json_file_storage import JSONFileStorage
from models.profile import Profile
from tests.test_models.test_common import TestCommon
import unittest


class TestJSONFileStorage(TestCommon):
    """
        Test JSON File Storage
    """

    @classmethod
    def setUpClass(self, className=JSONFileStorage):
        """
            Prepare JSON File Storage tests.
        """
        super().files.append('models/engine/json_file_storage.py')
        super().files.append(
            'tests/test_models/test_engine/test_json_file_storage.py')
        super().setUpClass(className)

    def setUp(self) -> None:
        """ Set up test environment """
        pass

    def test_save(self) -> None:
        storage = JSONFileStorage(
            {'profile': Profile(), 'category': Category()})
        file_path = "{}.json".format(datetime.strftime(datetime.utcnow(),
                                                       '%Y%m%d%H%M%S'))
        storage.save()
        self.assertTrue(os.path.isfile(file_path))
        os.remove(file_path)
        storage.save(file_path='toto.json')
        self.assertTrue(os.path.isfile('toto.json'))
        os.remove('toto.json')
