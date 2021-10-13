#!/usr/bin/python3
"""
    Test Survey Module.
"""
from models.survey import Survey
from tests.test_models.test_base_model import TestBaseModel


class TestSurvey(TestBaseModel):
    """
        Test Survey Model.
    """

    @classmethod
    def setUpClass(self):
        """
            Set up for docstring tests
        """

        super().files.append('models/survey.py')
        super().files.append('tests/test_models/test_survey.py')
        super().setUpClass(Survey)

    def test_wrong_name(self):
        """
            Test wrong name type insertion.
        """

        with self.assertRaises(TypeError) as context:
            obj = self.class_name()
            obj.name = 12

    def test_name_setter(self):
        """
            Test name setter method.
        """

        obj = self.class_name()
        obj.name = "toto"

        self.assertEqual("toto", obj.name)

    def test_to_dict(self):
        """
            Test to_dict() method.
        """

        obj = self.class_name(name="toto")
        super().test_to_dict()
        self.assertIn('name', obj.to_dict().keys())
        self.assertIn('toto', obj.to_dict().values())
