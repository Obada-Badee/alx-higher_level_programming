#!/usr/bin/python3

""" Empty class named aquares"""


class Square:
    """ Empty class Square that defines a square"""

    def __init__(self, size=0):
        """ Initializes the square class"""

        self.__size = size

    def area(self):
        """ Calculate the area of the square.

        Returns:
            The return value.The area of Square
        """

        return (self.__size ** 2)

    @property
    def size(self):
        """ Gets the size vlaue"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Sets the size vlaue"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if vlaue < 0:
            raise ValueError("size must be >= 0")

        self.__size = value