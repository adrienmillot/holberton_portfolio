#!/usr/bin/python3

class AnyResultException(Exception):

    def __init__(self, message="Any result found.") -> None:
        super().__init__(message)
