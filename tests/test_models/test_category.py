#!/usr/bin/python3
"""
    Test Category Module.
"""
from models.category import Category
from tests.test_models.test_base_model import TestBaseModel


class TestCategory(TestBaseModel):
    """
        Test Category Model.
    """

    @classmethod
    def setUpClass(self):
        """
            Set up for docstring tests
        """
        super().files.append('models/category.py')
        super().files.append('tests/test_models/test_category.py')
        super().setUpClass(Category)

    def test_wrong_name(self):
        """
            Test wrong name type insertion.
        """
        with self.assertRaises(Exception) as context:
            obj = self.className()
            obj.name = 12

    def test_name_setter(self):
        """
            Test name setter method.
        """
        obj = self.className()
        obj.name = "toto"

        self.assertEqual("toto", obj.name)

    def test_to_dict(self):
        """
            Test to_dict() method.
        """
        obj = self.className(name="toto")
        super().test_to_dict()
        self.assertIn('name', obj.to_dict().keys())
