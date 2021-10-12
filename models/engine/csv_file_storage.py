#!/usr/bin/python3
"""
    module CSV file storage.
"""

import csv
from datetime import datetime
from models.engine.file_storage import FileStorage


class CSVFileStorage(FileStorage):
    """
        CSV file storage class.
    """

    def __init__(self, obj_dict=...):
        """
           Constructor
        """

        file_path = "{}.csv".format(datetime.strftime(datetime.utcnow(),
                                                      '%Y%m%d%H%M%S'))
        super().__init__(obj_dict=obj_dict, file_path=file_path)

    def save(self, delimiter=";", file_path=None):
        """
           Save method.
        """

        file_path = self.file_path if file_path is None else file_path
        with open(file_path, 'w', newline='') as csv_file:
            spamwriter = csv.writer(csv_file, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for key, obj in self.objects.items():
                spamwriter.writerow(obj.__dict__.values())
