#!/usr/bin/python3

"""This module contains a Class named Rectangle
with a specific width an hieght"""


class Rectangle:
    """ A class that defines a Rectangle with specific width and height"""

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle class"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """ Return the width attribute"""

        return (self.__width)

    @width.setter
    def width(self, value):
        """ Set a new value for the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Return the height attribute"""

        return (self.__height)

    @height.setter
    def height(self, value):
        """ Set a new value for the height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def __str__(self):
        """A method to make a printable representation of the rectangle"""

        shape = ""
        if self.__width == 0 or self.__height == 0:
            return shape
        for row in range(self.__height):
            for col in range(self.__width):
                shape += "#"
            if (row != (self.__height - 1)):
                shape += "\n"
        return shape

    def __repr__(self):
        """ A method to display a rectangle """

        return f"Rectangle({self.__width}, {self.__height})"

    def area(self):
        """ Compute the area of the Rectangle object"""

        return (self.__width * self.__height)

    def perimeter(self):
        """ Compute the perimeter of the Rectangle object"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width*2 + self.__height*2)
