#!/usr/bin/python3
"""
Single module function.
This function adds two integers or floats.

"""


def add_integer(a, b=98):
    """
    Function to add two numbers.

    Args:
        a (int, float): first parameter, mandatory
        b (int, float): second parameter, 98 by default

    Return: added value.

    Raises:
        TypeError: when a parameter is not int nor float
        SyntaxError: when using invalid syntax
        OverflowError: when result is too large
        NameError: when using an undefined variable
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(a) is bool or a is None:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(b) is bool:
        raise TypeError("b must be an integer")
    if a != a or b != b:
        raise ValueError("cannot convert float NaN to integer")

    a = int(a)
    b = int(b)

    try:
        return a + b
    except SyntaxError:
        raise
    except OverflowError:
        raise OverflowError
    except NameError:
        raise NameError("undefined variable")
    except Exception as err:
        print("Unexpected error: ", err)
        raise
