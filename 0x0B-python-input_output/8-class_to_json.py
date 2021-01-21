#!/usr/bin/python3
"""This is a single class module."""


def class_to_json(obj):
    """Returns the dictionary description of obj."""
    if hasattr(obj, '__dict__'):
        return obj.__dict__
