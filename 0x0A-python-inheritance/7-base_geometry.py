#!/usr/bin/python3
"""This is a single class module.

The class BaseGeometry was purposefully left almost empty.
"""


class BaseGeometry():
    """This class was not left empty.

    Instead, it has a method which raises an exception,
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
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        pass
