#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.file_storage = FileStorage()
        FileStorage._FileStorage__file_path = self.file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_method(self):
        all_objects = self.file_storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_method(self):
        instance = BaseModel()
        key = "{}.{}".format(instance.__class__.__name__, instance.id)
        self.file_storage.new(instance)
        all_objects = self.file_storage.all()
        self.assertIn(key, all_objects)

    def test_save_method(self):
        instance = BaseModel()
        key = "{}.{}".format(instance.__class__.__name__, instance.id)
        self.file_storage.new(instance)
        self.file_storage.save()
        with open(self.file_path, 'r') as f:
            data = f.read()
            self.assertIn(key, data)

    def test_reload_method(self):
        instance = BaseModel()
        key = "{}.{}".format(instance.__class__.__name__, instance.id)
        self.file_storage.new(instance)
        self.file_storage.save()
        self.file_storage.reload()
        all_objects = self.file_storage.all()
        self.assertIn(key, all_objects)

    def test_reload_method_nonexistent_file(self):
        # Test that reloading a nonexistent file does not raise an error
        self.file_storage.reload()

    def test_reload_method_invalid_json(self):
        # Test that reloading an invalid JSON file does not raise an error
        with open(self.file_path, 'w') as f:
            f.write("Invalid JSON")
        self.file_storage.reload()


if __name__ == '__main__':
    unittest.main()
