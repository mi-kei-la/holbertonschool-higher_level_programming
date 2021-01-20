#!/usr/bin/python3
"""This is a single function module."""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string.

    Args:
        my_str: JSON string to decode.
    """
    decoded_str = json.loads(my_str)
    return decoded_str
