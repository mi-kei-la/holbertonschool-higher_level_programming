#!/usr/bin/python3
"""This is a single function module.

This function adds an attribute to a given object if possible.
"""


def add_attribute(object, name, value):
    """Add new attribute to object whenever possible."""
    setattr(object, name, value)
    if AttributeError:
        raise TypeError("can't add new attribute")
