#!/usr/bin/python3
"""
    File Storage module
"""

import os


class FileStorage:
    """Serialize to a file and deserializes"""

    __file_path = ""
    __objects = {}

    def __init__(self, obj_dict=None, file_path=''):
        """
            Constructor
        """
        self.objects = obj_dict
        self.file_path = file_path

    def save(self, file_path: str):
        """
            Save method.
        """

        raise NotImplemented('Save() method is not implemented.')

    @property
    def objects(self):
        """
            Objects getter method.
        """

        return self.__objects

    @objects.setter
    def objects(self, value: dict):
        """
            Objects setter method.
        """

        self.__objects = value

    @property
    def file_path(self):
        """
            File path getter method.
        """

        return self.__file_path

    @file_path.setter
    def file_path(self, value: dict):
        """
            File path setter method.
        """

        self.__file_path = value
