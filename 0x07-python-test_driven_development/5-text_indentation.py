#!/usr/bin/python3
"""
This is a single function module.
Print any given text with empty lines instead of special characters.
Special characters: period (.), colon (:), question mark (?).

"""


def text_indentation(text):
    """
    The function takes a string and prints it, replacing each period (.),
    colon (:) and question mark (?) for two empty lines.

    Args:
        text (str): text to be printed.

    Raises:
        TypeError: when text is not a string.
    """
    # Check parameter type (must be a string).
    if type(text) is not str:
        raise TypeError("text must be a string")

    # Make list of special characters to search.
    chars = ['.', ':', '?']
    # Convert text to list.
    listext = list(text)

    for c in chars:
        idx = 0
        spc = 0
        end = listext.count(c)
        while end:
            idx = listext.index(c, idx)
            if ' ' in listext:
                spc = listext.index(' ', idx)
                if idx + 1 == spc:
                    listext.pop(spc)
            listext.insert(idx + 1, "\n\n")
            idx += 3
            end -= 1

    # Print final text.
    print("".join(listext))

