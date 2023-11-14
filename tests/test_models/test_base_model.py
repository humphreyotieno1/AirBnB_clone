import unittest
from models.base_model import BaseModel
from datetime import datetime
from models import storage


class TestBaseModel(unittest.TestCase):
    def test_create_instance(self):
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)

    def test_id_generation(self):
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_save_method(self):
        instance = BaseModel()
        original_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(original_updated_at, instance.updated_at)

    def test_to_dict_method(self):
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['id'], instance.id)
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)

    def test_reload_method(self):
        instance = BaseModel()
        instance_dict = instance.to_dict()
        key = f"{instance.__class__.__name__}.{instance.id}"
        storage.save()
        storage.reload()
        reloaded_instance = storage.all()[key]
        self.assertEqual(reloaded_instance.to_dict(), instance_dict)


if __name__ == '__main__':
    unittest.main()
