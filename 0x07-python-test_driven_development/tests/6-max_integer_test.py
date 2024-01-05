#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 3, 4, 22]), 22)
        self.assertEqual(max_integer([11, 3, 4, 2]), 11)
        self.assertEqual(max_integer([1, 3, 5, 2, 3]), 5)
        self.assertEqual(max_integer([1, -3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
