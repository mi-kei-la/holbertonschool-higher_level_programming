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
    # Save text of Type Error as variable.
    te = "matrix must be a matrix (list of lists) of integers/floats"

    # Check type and value of parameters.
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError(te)

    # Save size of first row of matrix, as long as matrix is a list of lists.
    # If matrix is just one list, raise TypeError with message saved above.
    try:
        size = len(matrix[0])
    except TypeError:
        raise TypeError(te)

    # Check if all rows are the same size and of type list.
    for row in matrix:
        if type(row) is not list:
            raise TypeError(te)
        if len(row) == size:
            size = len(row)
        else:
            raise TypeError("Each row of the matrix must have the same size")

    # Create new matrix, and append the result of the division of
    # each value of the matrix by div, rounded to two decimal places.
    new = []
    for row in matrix:
        newrow = []
        for value in row:
            if type(value) in {int, float}:
                newrow.append(round(value / div, 2))
            else:
                raise TypeError(te)
        new.append(newrow)

    # Return new matrix.
    return new
