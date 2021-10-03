#!/usr/bin/python3
"""
    Test Common module.
"""
import inspect
import pep8 as pycodestyle
import unittest


class TestCommon(unittest.TestCase):
    """
        Tests to check the documentation and style class.
    """
    base_funcs = []
    files = [
        'tests/test_models/test_common.py'
    ]
    className = None

    @classmethod
    def setUpClass(self, className=None):
        """
            Set up for docstring tests
        """
        self.className = className
        self.base_funcs = inspect.getmembers(className, inspect.isfunction)

    def test_pep8_compliant(self):
        """
            Test for file compliancy with pep8.
        """
        for path in self.files:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(
                    errors, 0, '{} is not compliant with pep8.'.format(path)
                )

    def test_class_docstring(self):
        """
            Test for the BaseModel class docstring.
        """
        self.assertIsNot(
            self.__doc__, None,
            "{} class needs a docstring".format(self.__class__.__name__)
        )
        self.assertTrue(
            len(self.__doc__) >= 1,
            "{} class needs a docstring".format(self.__class__.__name__)
        )
        if self.className is not None:
            self.assertIsNot(
                self.className.__doc__, None,
                "{} class needs a docstring".format(self.className.__name__)
            )
            self.assertTrue(
                len(self.className.__doc__) >= 1,
                "{} class needs a docstring".format(self.className.__name__)
            )

    def test_func_docstrings(self):
        """
            Test for the presence of docstrings in BaseModel methods.
        """
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{}.{:s} method needs a docstring".format(
                        self.__class__.__name__, func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{}.{:s} method needs a docstring".format(
                        self.__class__.__name__, func[0])
                )
