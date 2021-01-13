#!/usr/bin/python3
"""
Single function module.
Print a square of n size.
Example: >>> print_square(3)
###
###
###

"""


def print_square(size):
    """This function prints a square of n size with '#'.

    Args:
        size: how many octathorpes (#) per side of the square

    Raises:
        TypeError: when size is not an integer
        ValueError: when size is less than 0
        OverflowError: when computing numbers that are too long
    """
    if type(size) is not int and type(size) is not float:
        raise TypeError("size must be an integer")

    size = int(size)

    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        pass
    else:
        try:
            for i in range(size):
                for j in range(size):
                    print("#", end='')
                print()
        except OverflowError:
            raise
