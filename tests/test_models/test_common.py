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
        # 'tests/test_models/test_common.py'
    ]
    class_name = None

    @classmethod
    def setUpClass(self, class_name=None):
        """
            Set up for docstring tests
        """

        self.class_name = class_name
        self.base_funcs = inspect.getmembers(class_name, inspect.isfunction)

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
            Test for the class docstring.
        """

        if self.class_name is not None:
            self.assertIsNot(
                self.class_name.__doc__, None,
                "{} class needs a docstring".format(self.class_name.__name__)
            )
            self.assertTrue(
                len(self.class_name.__doc__) >= 1,
                "{} class needs a docstring".format(self.class_name.__name__)
            )

    def test_func_docstrings(self):
        """
            Test for the presence of docstrings in class methods.
        """

        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{}.{:s} method needs a docstring".format(
                        self.class_name.__name__, func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{}.{:s} method needs a docstring".format(
                        self.class_name.__name__, func[0])
                )
