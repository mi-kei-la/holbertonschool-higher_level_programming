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
            name (str): always a string.
            value (int): positive integer.

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
    """This class instantiates Rectangle type objects.

    Methods:
        area: returns area of the rectangle.
    """
    def __init__(self, width, height):
        """This method initializes objects of type Rectangle.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Define the string method of this class."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Returns the area of the Rectangle object that calls it."""
        return self.__width * self.__height
