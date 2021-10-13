#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv


if getenv("SS_SERVER_MODE") == "API":
    from models.engine.db_storage import DBStorage
    db_storage = DBStorage()
    db_storage.reload()
