#!/usr/bin/python3
"""This function prints a square of n size with '#'.
Example: >>> print_square(3)
###
###
###

Returns nothing.
"""


def print_square(size):
    """Prints a square of n size.

    Args:
        size: how many octathorpes (#) per side of the square
    """
    if type(size) is not int and type(size) is not float:
        raise TypeError("size must be an integer")

    size = int(size)

    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        try:
            for i in range(size):
                for j in range(size):
                    print("#", end='')
                print()
        except OverflowError:
            raise
        except MemoryError:
            raise
