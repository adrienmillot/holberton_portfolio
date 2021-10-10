#!/usr/bin/python3
"""
    Test Proposal Module.
"""
from models.proposal import Proposal
from tests.test_models.test_base_model import TestBaseModel


class TestProposal(TestBaseModel):
    """
        Test Proposal Model.
    """

    @classmethod
    def setUpClass(self):
        """
            Set up for docstring tests
        """

        super().files.append('models/proposal.py')
        super().files.append('tests/test_models/test_proposal.py')
        super().setUpClass(Proposal)

    def test_wrong_label(self):
        """
            Test wrong label type insertion.
        """

        with self.assertRaises(Exception) as context:
            obj = self.class_name()
            obj.label = 12

    def test_label_setter(self):
        """
            Test label setter method.
        """

        obj = self.class_name()
        obj.label = "toto"

        self.assertEqual("toto", obj.label)

    def test_to_dict(self):
        """
            Test to_dict() method.
        """

        obj = self.class_name(label="toto")
        super().test_to_dict()
        self.assertIn('label', obj.to_dict().keys())
        self.assertIn('toto', obj.to_dict().values())
