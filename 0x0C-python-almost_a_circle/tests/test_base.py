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


    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        json_dictionary2 = Base.to_json_string(None)
        self.assertEqual(json_dictionary2, "[]")
        self.assertEqual(json_dictionary, '[{"id": 11, "width": 10, "height": 7, "x": 2, "y": 8}]')

        s1 = Square(10, 7, 2, 8)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        json_dictionary2 = Base.to_json_string(None)
        self.assertEqual(json_dictionary2, "[]")
        self.assertEqual(json_dictionary, '[{"id": 8, "size": 10, "x": 7, "y": 2}]')


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

        list_input2 = [
            {'id': 89, 'size': 10},
            {'id': 7, 'size': 1}
        ]
        json_list_input2 = Square.to_json_string(list_input2)
        list_output3 = Square.from_json_string(json_list_input2)
        self.assertEqual(list_output3, [{'id': 89, 'size': 10}, {'id': 7, 'size': 1}])


    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file(None)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            x = file.read()
            y = []
        self.assertEqual(x, '[{"id": 8, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 9, "width": 2, "height": 4, "x": 0, "y": 0}]')
        self.assertEqual(y, [])

        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        Square.save_to_file(None)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            x = file.read()
            y = []
        self.assertEqual(x, '[{"id": 8, "size": 10, "x": 7, "y": 2}, {"id": 10, "size": 2, "x": 4, "y": 0}]')
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

        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)


if __name__ == '__main__':
    unittest.main()
