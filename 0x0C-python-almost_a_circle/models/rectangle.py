#!/usr/bin/python3
"""This module contains a single class.

Class Rectangle: inherits from class Base.
"""
from models.base import Base


class Rectangle(Base):
    """This class defines a Rectangle object.

    Methods:
        setter and Getter methods for all arguments at creation.
        area: calculates the area of the Rectangle.
        display: print object.
        update: update several values.
        to_dictionary: return dictionary of arguments and values.
    """
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
        for y in range(self.y):
            print("")
        for h in range((self.__height)):
            for x in range(self.x):
                print(' ', end='')
            for w in range(self.__width):
                print('#', end='')
            print("")

    def update(self, *args, **kwargs):
        """Updates all values.
        Args should be in the following order:
            Id, Width, Height, x, y.
        """
        if args:
            if len(args) > 5:
                raise ValueError("function takes between 1 and 5 arguments," +
                                 " but {} were passed".format(len(args)))
            ats = ["id", "__width", "__height", "__x", "__y"]
            ar_list = []
            for arg in args:
                if type(arg) is not int:
                    raise TypeError("all arguments must be int")
                ar_list.append(arg)
            for i in range(len(ar_list)):
                setattr(self, ats[i], ar_list[i])
        else:
            for key in kwargs:
                if hasattr(self, key):
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        rect_dic = {}
        rect_dic["id"] = self.id
        rect_dic["width"] = self.width
        rect_dic["height"] = self.height
        rect_dic["x"] = self.x
        rect_dic["y"] = self.y
        return rect_dic
