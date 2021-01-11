#!/usr/bin/python3
"""
Single function module.
This function divides all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """Function to divide all values of a matrix by a given number.

    Args:
        matrix (list): list of lists containing ints or floats
        div (int, float): divisor for all values of the matrix

    Returns: new matrix of divided values

    Raises:
        TypeError: when div is not a number
                   when matrix is not a list of lists
                   when rows are not the same size
        ZeroDivisionError: when div is 0

    """
    te = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError(te)

    try:
        size = len(matrix[0])
    except TypeError:
        raise TypeError(te)

    for row in matrix:
        if type(row) is not list:
            raise TypeError(te)
        if len(row) == size:
            size = len(row)
        else:
            raise TypeError("Each row of the matrix must have the same size")

    new = []
    for row in matrix:
        newrow = []
        for value in row:
            if type(value) in {int, float}:
                newrow.append(round(value / div, 2))
            else:
                raise TypeError(te)
        new.append(newrow)

    return new
