#!/usr/bin/python3
""" Simple rectangle Module. """


class Rectangle:
    """ Class to define a rectangle. """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializing parameters.

        Arguments:
            height: (int) height of a rectangle.
            width : (int) width of a rectangle.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Getting the width of the rectangle & return it. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setting the width of the rectangle. """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getting the height of the rectangle & return it. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setting the height of the rectangle. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculating of the area of a rectangle & return the value. """
        return self.__height * self.__width

    def perimeter(self):
        """ Calculating of the perimeter of a rectangle & return the value. """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """ Return the string form for the rectangle represented by #. """
        if self.__height == 0 or self.__width == 0:
            return ""

        side = self.__width * str(self.print_symbol)
        return (side + "\n") * (self.__height - 1) + side

    def __repr__(self):
        """ Return the string form for the rectangle representation. """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Delete instance of Rectangle & printing message during that. """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method to return the biggest rectangle in area. """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Returns new instances to be squared shape. """
        return cls(size, size)
