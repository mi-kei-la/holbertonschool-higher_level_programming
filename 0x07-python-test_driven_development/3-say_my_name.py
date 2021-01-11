#!/usr/bin/python3
"""
Single function module.
This function prints a name.

"""


def say_my_name(first_name, last_name=""):
    """This function prints "My name is " followed by user given parameters.

    Args:
        first_name (str): mandatory first name
        last_name (str): empty string by default

    Raises:
        TypeError: when one or more parameters are not string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is " + first_name + " " + last_name)
