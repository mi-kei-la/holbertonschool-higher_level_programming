#!/usr/bin/python3
"""This module contains two classes.

Class:
    BaseGeometry: parent class.
    Rectangle: defines a rectangle.
"""


class BaseGeometry():
    """This class was not left empty.

    Instead, it has a method which raises an exception, \
    and a method to validate values.
    """
    def area(self):
        """Area is not implemented yet, so an exception is raised."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value parameter.

        Args:
            name: always a string.
            value: positive integer.

        Raises:
            TypeError:  if value is not an integer.
                        if name is not a string
            ValueError: if value is less or equal to 0.
        """
        if type(name) != str:
            raise TypeError("name must be a string")
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        pass


class Rectangle(BaseGeometry):
    """This class instantiates Rectangle type objects."""
    def __init__(self, width, height):
        """This method initializes objects of type Rectangle.

        Args:
            width: the width of the rectangle.
            height: the height of the rectangle.
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
