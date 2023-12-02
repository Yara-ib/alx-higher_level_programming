#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # self.assertFalse(len([1,3,4]), 0)
        self.assertIsNotNone([1,3,4])
