#!/usr/bin/python3

class WrongClassException(Exception):

    def __init__(self, obj, message="Not found.") -> None:
        message = "{} class not found.".format(obj.__class__.__name__)
        super().__init__(message)
