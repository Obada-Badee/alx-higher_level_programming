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
        """ Sets the size value"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """ Prints a square of "#" with the size given"""

        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
