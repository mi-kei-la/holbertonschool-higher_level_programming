#!/usr/bin/python3
"""This is a single function module.

is_same_class: check if a given object is \
exactly an instance of a given class.
"""


def is_same_class(obj, a_class):
    """Checks if obj is an instance of a_class.

    Args:
        obj: object to check.
        a_class: class object might or might not belong to.

    Returns:
        True if is instance, False otherwise.

    Raises:

    """
    if type(obj) is a_class:
        return True
    else:
        return False
