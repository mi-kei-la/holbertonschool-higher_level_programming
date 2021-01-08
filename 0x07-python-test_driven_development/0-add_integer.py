#!/usr/bin/python3
"""Function to add two integers or floats.

This function takes two arguments, a and b, and returns the added value.
The return is the added 
"""


def add_integer(a, b=98):
    """
    This function adds two numbers.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(a) is bool:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(b) is bool:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    try:
        return a + b
    except SyntaxError:
        raise

