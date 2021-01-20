#!/usr/bin/python3
"""This is a single function module."""
import json


def save_to_json_file(my_obj, filename):
    """Write the JSON representation of an object to a file.

    Args:
        my_obj: python object to encode and write.
        filename: filename to write to.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
