#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):
    def test_create_amenity(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)


if __name__ == '__main__':
    unittest.main()
