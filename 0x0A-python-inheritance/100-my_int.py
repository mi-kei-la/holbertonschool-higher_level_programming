#!/usr/bin/python3
"""This is a single class module.

Class:
    MyInt: inherits from int.
"""


class MyInt(int):
    """This class inherits from the class int.
    The main difference is that == is !=, and viceversa.
    """
    def __new__(self, value):
        """This creates a new instance of type MyInt."""
        self.value = value
        return self.value

    def __eq__(self, other):
        """This returns the equality of two operands."""
        return self.value != other.value

    def __ne__(self, value):
        """This returns the inequality of two operands."""
        return self.value == other.value
