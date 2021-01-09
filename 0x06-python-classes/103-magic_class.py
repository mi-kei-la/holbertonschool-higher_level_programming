#!/usr/bin/python3
"""This class mimics bytecode."""


class MagicClass:
    def __init__(self, radius=0):
        """
        initialize bytecode.
        """
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """calculate area"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """calculate circumference"""
        return 2 * math.pi * self._MagicClass__radius
