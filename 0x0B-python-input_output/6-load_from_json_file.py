#!/usr/bin/python3
"""This is a single function module."""
import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file.

    Args:
        filename: file to read from.
    """
    with open(filename, "r") as f:
        obj = json.load(f)
    return obj
