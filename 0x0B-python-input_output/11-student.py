#!/usr/bin/python3
"""This module defines the class Student."""


class Student:
    """Class Student."""
    def __init__(self, first_name, last_name, age):
        """Initializes instance of type Student."""
        if type(first_name) != str or type(last_name) != str:
            raise TypeError("first and last name must be strings")
        if type(age) != int:
            raise TypeError("age must be an int")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns attributes of an object."""
        if attrs is None:
            if hasattr(self, '__dict__'):
                return self.__dict__
        else:
            ats = {}
            for at in attrs:
                if hasattr(self, at):
                    ats[at] = getattr(self, at)
            return ats

    def reload_from_json(self, json):
        """Replace all attributes with json attributes."""
        for ats in json:
            if hasattr(self, ats):
                val = json[ats]
                setattr(self, ats, val)
