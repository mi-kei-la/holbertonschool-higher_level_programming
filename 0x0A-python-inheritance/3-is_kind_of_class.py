#!/usr/bin/python3
"""This is a single function module.

is_kind_of_class: check if a given object is instance of a class.
"""


def is_kind_of_class(obj, a_class):
    """Checks if a given object is instance of a given class.
    
    Args:
        obj: object to check.
        a_class: class given.

    Returns:
        True if it's instance, False otherwise.
    """
    return isinstance(obj, a_class)
