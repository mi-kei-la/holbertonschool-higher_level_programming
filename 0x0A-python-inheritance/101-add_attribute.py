#!/usr/bin/python3
"""This is a single function module.

This function adds an attribute to a given object if possible.
"""


def add_attribute(obj, name, value):
    """Add new attribute to object whenever possible."""
    if hasattr(obj, name) is True:
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
