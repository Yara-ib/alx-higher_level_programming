#!/usr/bin/python3
"""Unittest for Rectangle Class """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

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

    def test_area(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.area(), 20)

if __name__ == '__main__':
    unittest.main()
