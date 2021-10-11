#!/usr/bin/python3
"""
    Bla
"""


from datetime import datetime
import json
from models.engine.file_storage import FileStorage


class JSONFileStorage(FileStorage):
    """
        Bla
    """

    def __init__(self, obj_dict=...):
        """
           Bla
        """
        file_path = "{}.json".format(datetime.strftime(datetime.utcnow(),
                                                       '%Y%m%d%H%M%S'))
        super().__init__(obj_dict=obj_dict, file_path=file_path)

    def save(self, file_path=None):
        """
           Bla
        """

        file_path = self.file_path if file_path is None else file_path
        with open(file_path, 'w') as file:
            for key, obj in self.objects.items():
                json.dump(obj.to_dict(), file)
