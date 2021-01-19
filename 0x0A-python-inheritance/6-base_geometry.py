#!/usr/bin/python3
"""This is a single class module.

The class BaseGeometry was purposefully left almost empty.
"""


class BaseGeometry():
    """This class was not left empty.

    Instead, it has a single method, which raises an exception.
    """
    def area(self):
        """Area is not implemented yet, so an exception is raised."""
        raise Exception("area() is not implemented")
