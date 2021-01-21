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

    def to_json(self):
        """Returns the dictionary description of an object."""
        if hasattr(self, '__dict__'):
            return self.__dict__
