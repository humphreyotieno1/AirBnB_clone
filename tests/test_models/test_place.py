#!/usr/bin/python3
import unittest
from models.place import Place
from models import storage


class TestPlace(unittest.TestCase):
    def test_create_place(self):
        place = Place()
        self.assertIsInstance(place, Place)


if __name__ == '__main__':
    unittest.main()
