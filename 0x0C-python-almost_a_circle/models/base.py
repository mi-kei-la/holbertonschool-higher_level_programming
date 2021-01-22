#!/usr/bin/python3
"""This module contains the Base class."""


class Base():
    """This class gives all instances an id."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor, assigns ID."""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
