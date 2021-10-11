#!/usr/bin/python3
"""
    File Storage test Module
"""
from datetime import datetime
import os
from models.category import Category
from models.profile import Profile
from models.engine.csv_file_storage import CSVFileStorage
from tests.test_models.test_common import TestCommon
import unittest


class TestCSVFileStorage(TestCommon):
    """
        Test CSV File Storage
    """

    @classmethod
    def setUpClass(self, className=CSVFileStorage):
        """
            Prepare CSV File Storage tests.
        """
        super().files.append('models/engine/csv_file_storage.py')
        super().files.append(
            'tests/test_models/test_engine/test_csv_file_storage.py')
        super().setUpClass(className)

    def test_save(self) -> None:
        storage = CSVFileStorage(
            {'profile': Profile(), 'category': Category()})
        file_path = "{}.csv".format(datetime.strftime(datetime.utcnow(),
                                                      '%Y%m%d%H%M%S'))
        storage.save()
        self.assertTrue(os.path.isfile(file_path))
        os.remove(file_path)
        storage.save(file_path='toto.csv')
        self.assertTrue(os.path.isfile('toto.csv'))
        os.remove('toto.csv')
