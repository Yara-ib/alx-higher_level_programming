#!/usr/bin/python3
"""Unittest for Square Class """
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_size(self):
        self.assertRaises(TypeError, lambda: Square("10"))
        self.assertRaises(ValueError, lambda: Square(-2))
        self.assertRaises(TypeError, lambda: Square(2.5))

    def test_x(self):
        self.assertRaises(ValueError, lambda: Square(2, -3, 1))
        self.assertRaises(TypeError, lambda: Square(5, {10}, 3))

    def test_y(self):
        self.assertRaises(ValueError, lambda: Square(2, 3, -1))
        self.assertRaises(TypeError, lambda: Square(5, 10, {}))

    def test_area(self):
        r3 = Square(10, 0, 0, 12)
        self.assertEqual(r3.area(), 100)
