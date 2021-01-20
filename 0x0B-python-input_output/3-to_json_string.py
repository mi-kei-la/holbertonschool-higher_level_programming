#!/usr/bin/python3
"""This is a single function module."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation (string) of an object."""
    json_string = json.dumps(my_obj)
    return json_string
