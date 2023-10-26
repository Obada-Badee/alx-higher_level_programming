#!/usr/bin/python3

""" Empty class named aquares"""


class Square:
    """ Empty class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """ Initializes the square class"""

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Gets the position vlaue"""

        return (self.__position)

    @position.setter
    def position(self, value):
        """ Change the position"""

        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """ Prints a square of "#" with the size given"""

        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)]))
