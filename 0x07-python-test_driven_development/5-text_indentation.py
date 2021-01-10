#!/usr/bin/python3
"""This is a single function module.
The function takes a string of any size and prints it,
swapping each period (.), double colon (:) and question mark (?)
for two empty lines.

Returns nothing.
"""


def text_indentation(text):
    """
    Print text with empty lines instead of special characters.
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
