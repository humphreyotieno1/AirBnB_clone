#!/usr/bin/python3
import unittest
from models.state import State
from models import storage


class TestState(unittest.TestCase):
    def test_create_state(self):
        state = State()
        self.assertIsInstance(state, State)


if __name__ == '__main__':
    unittest.main()
