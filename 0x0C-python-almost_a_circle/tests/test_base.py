#!/usr/bin/python3
"""Unittest for Base Class """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    def test_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_width(self):
        self.assertRaises(TypeError, lambda: Rectangle("10", 2))
        self.assertRaises(ValueError, lambda: Rectangle(-2, 2))
        self.assertRaises(TypeError, lambda: Rectangle(2.5, 5))

    def test_height(self):
        self.assertRaises(TypeError, lambda: Rectangle(10, "2"))
        self.assertRaises(ValueError, lambda: Rectangle(2, -5))
        self.assertRaises(TypeError, lambda: Rectangle(5, 5.5))

    def test_x(self):
        self.assertRaises(ValueError, lambda: Rectangle(10, 2, -3, 1))
        self.assertRaises(TypeError, lambda: Rectangle(2, 5, {10}, 3))

    def test_y(self):
        self.assertRaises(ValueError, lambda: Rectangle(10, 2, 3, -1))
        self.assertRaises(TypeError, lambda: Rectangle(2, 5, 10, {}))

    def test_to_json_string(self):
        # # dictionary = Rectangle(10, 7, 2, 8).to_dictionary()
        # json_dictionary = Base.to_json_string({"x": 2, "width": 10, "id": 1, "height": 7, "y": 8})
        # # self.assertEqual(type(json_dictionary), str)
        # self.assertEqual(json_dictionary, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')

        json_dictionary2 = Base.to_json_string(None)
        self.assertEqual(json_dictionary2, "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

if __name__ == '__main__':
    unittest.main()
