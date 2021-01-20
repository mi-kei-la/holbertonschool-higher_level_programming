#!/usr/bin/python3
"""This is a single function module."""


def read_file(filename=""):
    """Reads a given file and prints it to standard output.

    Args:
        filename: file to open.
    """
    with open(filename, encoding="UTF-8") as f:
        for line in f:
            print(line, end='')
