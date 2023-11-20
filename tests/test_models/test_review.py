#!/usr/bin/python3
import unittest
from models.review import Review
from models import storage


class TestReview(unittest.TestCase):
    def test_create_review(self):
        review = Review()
        self.assertIsInstance(review, Review)

    # Add more test cases for Review class...


if __name__ == '__main__':
    unittest.main()
