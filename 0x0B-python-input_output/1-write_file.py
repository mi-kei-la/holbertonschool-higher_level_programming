#!/usr/bin/python3
"""This is a single function module."""


def write_file(filename="", text=""):
    """Writes a given string to a text file.

    Args:
        filename: file to write text to.
            If filename does not exist, it will be created.
            If it exists, it will be overwritten.
        text: text to write to file.

    Returns:
        number of characters written.
    """
    with open(filename, "w+", encoding="UTF-8") as f:
        count = f.write(text)
    return count
