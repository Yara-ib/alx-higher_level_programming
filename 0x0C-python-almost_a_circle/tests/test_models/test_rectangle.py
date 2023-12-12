#!/usr/bin/python3
"""Unittest for Rectangle Class """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_area(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.area(), 20)

if __name__ == '__main__':
    unittest.main()
