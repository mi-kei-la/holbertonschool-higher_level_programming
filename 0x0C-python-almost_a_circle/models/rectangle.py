#!/usr/bin/python3
"""This module contains a single class.

Class Rectangle: inherits from class Base.
"""
from models.base import Base


class Rectangle(Base):
    """This class defines a Rectangle object."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instance, checking input."""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width musth be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Width getter."""
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter."""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width musth be > 0")
        self.__width = width

    @property
    def height(self):
        """Height getter."""
        return self.__height

    @height.setter
    def height(self, height):
        """Height setter."""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """X getter."""
        return self.__x

    @x.setter
    def x(self, x):
        """X setter."""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Y value getter."""
        return self.__y

    @y.setter
    def y(self, y):
        """Y value setter."""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def __str__(self):
        """String representation of object Rectangle."""
        return "[Rectangle] ({}) \
{}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def area(self):
        """Returns area of rectangle."""
        return self.__height * self.__width

    def display(self):
        """Prints rectangle with # characters."""
        if self.__y > 0:
            for y in range(self.__y):
                print("")
        for h in range((self.__height)):
            if self.__y > 0:
                for y in range(self.__y):
                    print(' ', end='')
            for w in range(self.__width):
                print('#', end='')
            print("")

    def update(self, *args):
        """Updates all values.
        Args should be in the following order:
            Id
            Width
            Height
            X
            Y
        """
        
