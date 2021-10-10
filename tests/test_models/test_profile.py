#!/usr/bin/python3
"""
    Test Profile Module.
"""
from datetime import datetime
from models.profile import Profile
from tests.test_models.test_base_model import TestBaseModel


class TestProfile(TestBaseModel):
    """
        Test Profile Model.
    """

    @classmethod
    def setUpClass(self):
        """
            Set up for docstring tests
        """
        super().files.append('models/profile.py')
        super().files.append('tests/test_models/test_profile.py')
        super().setUpClass(Profile)

    def setUp(self) -> None:
        self.wrong_born_at_kwargs = {
            'last_name': 'toto',
            'first_name': 'titi',
            'gender': 'tata',
            'born_at': '2021-10-10T12:32:00'
        }
        tic = datetime.utcnow()
        strtic = tic.strftime('%Y-%m-%dT%H:%M:%S.%f')
        self.kwargs = {
            'last_name': 'toto',
            'first_name': 'titi',
            'gender': 'tata',
            'born_at': strtic
        }

    def test_wrong_last_name(self):
        """
            Test wrong last name type insertion.
        """

        with self.assertRaises(Exception) as context:
            obj = self.class_name()
            obj.last_name = 12

    def test_wrong_first_name(self):
        """
            Test wrong first name type insertion.
        """

        with self.assertRaises(Exception) as context:
            obj = self.class_name()
            obj.first_name = 12

    def test_wrong_gender(self):
        """
            Test wrong gender type insertion.
        """

        with self.assertRaises(Exception) as context:
            obj = self.class_name()
            obj.gender = 12

        with self.assertRaises(Exception) as context:
            obj = self.class_name()
            obj.gender = 'toto'

    def test_wrong_born_at(self):
        """
            Test wrong first name type insertion.
        """

        with self.assertRaises(Exception) as context:
            obj = self.class_name()
            obj.born_at = 12

    def test_last_name_setter(self):
        """
            Test last name setter method.
        """

        obj = self.class_name()
        obj.last_name = "toto"

        self.assertEqual("toto", obj.last_name)

    def test_first_name_setter(self):
        """
            Test first name setter method.
        """

        obj = self.class_name()
        obj.first_name = "toto"

        self.assertEqual("toto", obj.first_name)

    def test_gender_setter(self):
        """
            Test gender setter method.
        """

        obj = self.class_name()
        obj.gender = "Male"

        self.assertEqual("Male", obj.gender)
        obj.gender = "male"

        self.assertEqual("Male", obj.gender)

    def test_to_dict(self):
        """
            Test to_dict() method.
        """

        obj = self.class_name(
            last_name="toto", first_name="titi", gender="tata")
        super().test_to_dict()
        self.assertIn('last_name', obj.to_dict().keys())
        self.assertIn('toto', obj.to_dict().values())
        self.assertIn('first_name', obj.to_dict().keys())
        self.assertIn('titi', obj.to_dict().values())
        self.assertIn('gender', obj.to_dict().keys())
        self.assertIn('tata', obj.to_dict().values())

    def test_born_at_init(self):
        """
            Test born_at init.
        """

        kwargs = {}
        tic = datetime.utcnow()
        majority_year = tic.year - 18
        majority_tic = tic.replace(year=majority_year)
        str_tic = tic.strftime('%Y-%m-%dT%H:%M:%S.%f')
        majority_str_tic = majority_tic.strftime('%Y-%m-%dT%H:%M:%S.%f')
        with self.assertRaises(Exception) as context:
            kwargs['born_at'] = tic
            obj = self.class_name(**kwargs)
        with self.assertRaises(ValueError) as context:
            kwargs['born_at'] = str_tic
            obj = self.class_name(**kwargs)
        kwargs['born_at'] = majority_str_tic
        obj = self.class_name(**kwargs)
        self.assertNotEqual(obj.born_at, majority_str_tic)
        self.assertEqual(obj.born_at, majority_tic)
