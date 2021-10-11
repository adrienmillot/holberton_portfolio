#!/usr/bin/python3
"""
    Test DBStorage module.
"""


from os import getenv
import unittest
from models.category import Category
from models.engine.db_storage import DBStorage
from models.user import User
from tests.test_models.test_engine.test_common_storage import TestCommonStorage


@unittest.skipIf(
    getenv('SS_SERVER_MODE') != 'API', 'Test only for server api mode'
)
class TestDBStorage(TestCommonStorage):
    """
        Test database storage model.
    """

    @classmethod
    def setUpClass(self, className=DBStorage):
        """
            Prepare db storage tests.
        """

        super().files.append('models/engine/db_storage.py')
        super().files.append(
            'tests/test_models/test_engine/test_db_storage.py'
        )
        super().setUpClass(className)

    def setUp(self) -> None:
        """
            Set Up a User class for Database storage testing.
        """
        from models import db_storage
        self.storage = db_storage
        self.user_length = len(self.storage.all(User))

    def test_all_method(self):
        """
            Test the all() method of DB Storage.
        """

        obj_dict = self.storage.all()
        self.assertIsInstance(obj_dict, dict, "")
        self.assertDictEqual(obj_dict, {})
        obj_user = User(username='toto', password='titi')
        obj_category = Category(name='tata')
        self.storage.new(obj_user)
        self.storage.new(obj_category)
        self.storage.save()
        all_users = self.storage.all(User)
        self.assertIn(obj_user, all_users.values())
        self.assertNotIn(obj_category, obj_dict)
        self.storage.delete(obj_user)
        self.storage.delete(obj_category)
        self.storage.save()

    def test_new_method(self):
        """
            Test the new() method of DB Storage.
        """

        self.assertEqual(0, self.user_length)
        obj_user = User(username='toto', password='titi')
        self.storage.new(obj_user)
        self.storage.save()
        all_users = self.storage.all(User)
        self.assertIn(obj_user, all_users.values())
        self.assertEqual(1, self.user_length + 1)
        self.storage.delete(obj_user)
        self.storage.save()

    def test_delete_method(self):
        """
            Test the delete() method of DB Storage.
        """
        obj_user = User(username='toto', password='titi')
        self.storage.new(obj_user)
        self.storage.save()
        all_users = self.storage.all(User)
        self.assertIn(obj_user, all_users.values())
        self.storage.delete(obj_user)
        self.storage.save()
        all_users = self.storage.all(User)
        self.assertNotIn(obj_user, all_users.values())

    def test_get_method(self):
        """
            Test the get() method of DB Storage.
        """

        obj_user = User(username='toto', password='titi')
        self.storage.new(obj_user)
        self.storage.save()
        obj_user_from_db = self.storage.get(User, obj_user.id)
        self.assertEqual(obj_user, obj_user_from_db)
        self.storage.delete(obj_user)
        self.storage.save()

    def test_count_method(self):
        """
            Test the count() method of DB Storage.
        """

        init_count = self.storage.count()
        obj_user = User(username='toto', password='titi')
        self.storage.new(obj_user)
        self.storage.save()
        self.assertEqual(self.storage.count(), init_count + 1)
        self.storage.delete(obj_user)
        self.storage.save()

    def test_save_method(self):
        """
            Test the save() method of DB Storage.
        """

        obj_user = User(username='toto', password='titi')
        all_users = self.storage.all(User)
        self.assertNotIn(obj_user, all_users.values())
        self.storage.new(obj_user)
        self.storage.save()
        all_users = self.storage.all(User)
        self.assertIn(obj_user, all_users.values())
        self.storage.delete(obj_user)
        self.storage.save()

    def test_close_method(self):
        pass
