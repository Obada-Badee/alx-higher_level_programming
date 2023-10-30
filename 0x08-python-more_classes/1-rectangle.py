#!/usr/bin/python3

"""
This modle definse a class Rectangle
"""


class Rectangle:
    """
    A class that deifnes a Rectangle
    """

    def __init__(self, width=0, height=0):
        """ Initilze the width and height"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """ Returns the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the vlaue of the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if vlaue < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Returns the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the vlaue of the height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if vlaue < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
