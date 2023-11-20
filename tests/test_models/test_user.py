#!/usr/bin/python3
import unittest
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    def test_create_user(self):
        user = User()
        self.assertIsInstance(user, User)


if __name__ == '__main__':
    unittest.main()
