#!/usr/bin/python3
"""Unittest for Base Class """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        json_dictionary2 = Base.to_json_string(None)
        self.assertEqual(json_dictionary2, "[]")
        self.assertEqual(json_dictionary, '[{"id": 10, "width": 10, "height": 7, "x": 2, "y": 8}]')

    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        list_output2 = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'id': 89, 'width': 10, 'height': 4}, {'id': 7, 'width': 1, 'height': 7}])
        self.assertEqual(list_output2, [])

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            x = file.read()
            y = []
        self.assertEqual(x, '[{"id": 8, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 9, "width": 2, "height": 4, "x": 0, "y": 0}]')
        self.assertEqual(y, [])

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        output = "[Rectangle] (4) 2/8 - 10/7"
        for rect in list_rectangles_input:
            self.assertEqual("{}".format(rect), output)
        list_rectangles_output2 = []
        self.assertEqual("{}".format(list_rectangles_output2), "[]")

        s1 = Square(5)
        list_squares_input = [s1]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        output2 = "[Square] (6) 0/0 - 5"
        for square in list_squares_output:
            self.assertEqual("{}".format(square), output2)
        list_squares_output2 = []
        self.assertEqual("{}".format(list_squares_output2), "[]")


    def create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)


if __name__ == '__main__':
    unittest.main()
