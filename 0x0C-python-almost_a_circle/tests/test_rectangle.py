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

    def test_display(self):
        self.assertNotEqual(Rectangle(3, 2, 1, 0).display(), "##\n##\n##")

    def test_to_dictionary(self):
        self.assertEqual(Rectangle(10, 2, 1, 9).to_dictionary(), {'id': 12, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(Rectangle.__str__(r1), "[Rectangle] (89) 3/1 - 2/10")


if __name__ == '__main__':
    unittest.main()
