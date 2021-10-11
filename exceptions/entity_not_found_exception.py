#!/usr/bin/python3

class EntityNotFoundException(Exception):

    def __init__(self, cls, message="Not found.") -> None:
        message = "{} entity not found.".format(cls.__class__.__name__)
        super().__init__(message)
