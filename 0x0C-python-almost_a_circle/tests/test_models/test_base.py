#!/usr/bin/python3
"""Unittest for Base Class """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_to_json_string(self):
        dictionary = Rectangle(10, 7, 2, 8).to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)

        dictionary2 = Rectangle().to_dictionary()
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, [])

if __name__ == '__main__':
    unittest.main()
