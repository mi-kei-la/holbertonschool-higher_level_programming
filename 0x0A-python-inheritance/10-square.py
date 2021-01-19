#!/usr/bin/python3
"""This module defines a single class."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """This class instantiates an object of type Square.

    Methods:
        area: returns the area of the calling square.
    """
    def __init__(self, size):
        """Creates an object of type square, validating the parameters.

        Args:
            size (int): size of each side of the square.
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
