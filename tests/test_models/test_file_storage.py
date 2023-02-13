#!/usr/bin/python3

# UNIT TESTS

import os
import unittest
from models.user import User

from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    # File Storage Test
    def test_all(self):
        storage = FileStorage()
        self.assertEqual(type(storage.all()), dict)

    def test_new(self):
        storage = FileStorage()
        storage.new(User("test@email.com", "test", "test", "test"))
        self.assertEqual(type(storage.all()), dict)

    def test_save(self):
        storage = FileStorage()
        storage.new(User("test@email.com", "test", "test", "test"))
        storage.save()
        self.assertEqual(type(storage.all()), dict)

    def test_reload(self):
        storage = FileStorage()
        storage.reload()
        self.assertEqual(type(storage.all()), dict)

        # os.remove(filename)


# create base_model.py
# create
