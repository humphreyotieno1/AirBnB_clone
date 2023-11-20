#!/usr/bin/python3
import unittest
from models.city import City
from models import storage


class TestCity(unittest.TestCase):
    def test_create_city(self):
        city = City()
        self.assertIsInstance(city, City)

if __name__ == '__main__':
    unittest.main()
