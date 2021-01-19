#!/usr/bin/python3
"""This is a single module class."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """This class instantiates Rectangle type objects."""
    def __init__(self, width, height):
        """This method initializes objects of type Rectangle.

        Args:
            width: the width of the rectangle.
            height: the height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
