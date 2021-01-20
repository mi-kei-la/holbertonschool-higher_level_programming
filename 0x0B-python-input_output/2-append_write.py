#!/usr/bin/python3
"""This is a single function module."""


def append_write(filename="", text=""):
    """Append a given text to a file.

    Args:
        filename: name of the file.
            If the file doesn't exist, it should be created.
        text: text to append to file.

    Returns:
        number of characters written.
    """
    with open(filename, "a+", encoding="UTF-8") as f:
        count = f.write(text)
        return count
