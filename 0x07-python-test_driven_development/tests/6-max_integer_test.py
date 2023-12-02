#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertTrue([1, 3, 4, 2], 4)

    def test_max_integer2(self):
        self.assertTrue([1, 3, 4, 22], 22)

    def test_max_integer3(self):
        self.assertTrue([11, 3, 4, 2], 11)
        self.assertTrue([1, 3, 5, 2, 3], 5)
        self.assertTrue([1, -3, 4, 2], 4)
        self.assertTrue([-1, -3, -4, -2], -1)
        self.assertTrue([1], 1)
        self.assertFalse([], 0)
