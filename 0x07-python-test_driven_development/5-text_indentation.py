#!/usr/bin/python3
"""This is a single function module.
Print any given text with empty lines instead of special characters.

"""


def text_indentation(text):
    """
    The function takes a string and prints it, replacing each period (.),\
    double colon (:) and question mark (?) for two empty lines.

    Args:
        text (str): text to be printed

    Raises:
        TypeError: when text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = False

    for x in text:
        if (x is not '.' and x is not ':' and x is not '?'):
            if flag is False:
                print(x, end="")
            else:
                flag = False
                continue
        else:
            print(x)
            print()
            flag = True
