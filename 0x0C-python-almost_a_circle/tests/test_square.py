#!/usr/bin/python3
"""Unittest for Square Class """
import unittest
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
        self.assertEqual(Square(10, 0, 0, 12).area(), 100)

    def test_to_dictionary(self):
        self.assertEqual(Square(10, 2, 1).to_dictionary(), {'id': 14, 'size': 10, 'x': 2, 'y': 1})

    def test_update(self):
        s1 = Square(5)
        s1.update(size=7, id=89, y=1)
        self.assertEqual(Square.__str__(s1), "[Square] (89) 0/1 - 7")


if __name__ == '__main__':
    unittest.main()
