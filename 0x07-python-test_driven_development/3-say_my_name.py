#!/usr/bin/python3
"""This function prints "My name is" followed by first and last name.

Parameters must be strings, and there should be at least one parameter.
"""


def say_my_name(first_name, last_name=""):
    """Prints text with user parameters.

    Args:
        first name: string
        last name: string, not required
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is " + first_name + " " + last_name)
