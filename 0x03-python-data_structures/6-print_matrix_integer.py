#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) == 0:
            print("")
        else:
            a = 0
            for value in row:
                a = a + 1
                if a < len(row):
                    print("{:d}" .format(value), end=" ")
                else:
                    print("{:d}" .format(value))
