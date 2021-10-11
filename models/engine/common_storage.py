#!/usr/bin/python3
"""
    Common Storage abstract methods Module
"""

from abc import ABC, abstractmethod


class CommonStorage(ABC):
    """
        Abstract Classes for Storage methods.
    """

    @abstractmethod
    def all(self, cls=None):
        """
            Return a dictionary representation of all objects
            from a class (or all if not specified).
        """

        raise NotImplemented("All method is not implemented.")

    @abstractmethod
    def close(self):
        """
            Call reload() method for deserializing the JSON file to objects
        """

        raise NotImplemented("Close method is not implemented.")

    @abstractmethod
    def count(self, cls=None):
        """
            Count the number of objects in storage
        """

        raise NotImplemented("Count method is not implemented.")

    @abstractmethod
    def delete(self, obj=None):
        """
            Delete obj from __objects if it’s inside
        """

        raise NotImplemented("Delete method is not implemented.")

    @abstractmethod
    def get(self, cls, id):
        """
            Returns the object based on the class name and its ID, or
            None if not found
        """

        raise NotImplemented("Get method is not implemented.")

    @abstractmethod
    def new(self, obj):
        """
            Add a new object to storage.
        """

        raise NotImplemented("New method is not implemented.")

    @abstractmethod
    def reload(self):
        """
            Refresh cache object list.
        """

        raise NotImplemented("Reload method is not implemented.")

    @abstractmethod
    def save(self):
        """
            Register staged objects.
        """

        raise NotImplemented("Save method is not implemented.")
