#!/usr/bin/python3
"""This module defines the class Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The following code defines the class square."""
    def __init__(self, size, x=0, y=0, id=None):
        """This creates a new instance of this class."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """This defines the string method."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """Returns the size of a square."""
        return self.width

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width musth be > 0")
        self.__width = size

    def update(self, *args, **kwargs):
        """Updates all values.
        Args should be in the following order:
            Id
            Size
            X
            Y
        """
        if args:
            if len(args) > 4:
                raise ValueError("function takes between 1 and 4 " +
                                 "arguments, but {} were " +
                                 "passed".format(len(args)))
            ats = ["id", "width", "x", "y"]
            ar_list = []
            for arg in args:
                if type(arg) is not int:
                    raise TypeError("all arguments must be int")
                ar_list.append(arg)
            for i in range(len(ar_list)):
                setattr(self, ats[i], ar_list[i])
        else:
            for key in kwargs:
                if type(key) is str and type(kwargs[key]) is int:
                    if hasattr(self, key):
                        if key == "size":
                            setattr(self, "width", kwargs[key])
                        else:
                            setattr(self, key, kwargs[key])
                else:
                    raise TypeError("all values must be int")

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        sq_dic = {}
        sq_dic["id"] = self.id
        sq_dic["size"] = self.width
        sq_dic["x"] = self.x
        sq_dic["y"] = self.y
        return sq_dic
