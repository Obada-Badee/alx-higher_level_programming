#!/usr/bin/python3

"""
This modle definse a class Rectangle
"""


class Rectangle:
    """
    Empty class that deifnes a Rectangle
    """

    def __init__(self, width=0, height=0):
        """ Initilze the width and height"""

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Returns the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the vlaue of the width"""

        if not isinstance(int, value):
            raise TypeError("width must be an integer")
        elif vlaue < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Returns the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the vlaue of the height"""

        if not isinstance(int, value):
            raise TypeError("height must be an integer")
        elif vlaue < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
