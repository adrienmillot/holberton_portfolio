#!/usr/bin/python3

class AttributeNotFoundException(Exception):

    def __init__(self, attribute: str, message="Not found.") -> None:
        message = "Missing {}.".format(attribute)
        super().__init__(message)
