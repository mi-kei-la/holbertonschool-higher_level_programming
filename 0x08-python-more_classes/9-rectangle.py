#!/usr/bin/python3
"""
Class:
    Rectangle: defines a rectangle of a given height and width

"""


class Rectangle:
    """This class defines a rectangle of given width and height.

    Attributes:
        number_of_instances: counts the rectangles.
        print_symbol: symbol used for the string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize object of type Rectangle.
        Adds 1 to number_of_instances

        Attributes:
            __width(int): width of the rectangle.
            __height(int): height of the rectangle.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Retrieve value of width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set value of width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve value of height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set value of height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return value of area of rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return value of perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the string representation of a Rectangle instance."""
        ret = ""
        symbol = str(self.print_symbol)
        if self.__width == 0 or self.__height == 0:
            return ret
        else:
            for h in range(self.__height):
                for w in range(self.__width):
                    ret += symbol
                if h != (self.__height - 1):
                    ret += '\n'
        return ret

    def __repr__(self):
        """Return the formal representation of the rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Delete an instance of type square."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare area of two rectangles.

        Args:
            rect_1(Rectangle): parameter
            rect_2(Rectangle): parameter

        Returns:
            largest rectangle, or rect_1 if equal.

        Raises:
            TypeError: when one or more arguments are not rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Create a rectangle with height equal to width.

        Args:
            size(int): size of each side of the square.

        Returns: new rectangle
        """
        return cls(size, size)
