#!/usr/bin/python3
"""This is a single function module.

inherits_from: returns true if the given object belongs \
to a subclass of a given class.
"""


def inherits_from(obj, a_class):
    """Checks if a given object belongs to a subclass of a given class.

    Args:
        obj: given object.
        a_class: class to check subclasses.

    Returns:
        True if object belongs to a subclass of a_class, False otherwise.
    """
    if isinstance(obj, a_class) is True and type(obj) != a_class:
        return True
    else:
        return False
