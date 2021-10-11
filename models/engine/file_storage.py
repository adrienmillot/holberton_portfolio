#!/usr/bin/python3
"""
    File Storage module
"""

import os


class FileStorage:
    """Serialize to a file and deserializes"""

    __file_path = ""
    __objects = {}

    def __init__(self, obj_dict={}, file_path=''):
        """
        Bla
        """
        self.objects = obj_dict
        self.file_path = file_path

    def save(self, data:str, path:str):
        raise NotImplemented('Save() method is not implemented.')

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, value: dict):
        self.__objects = value
