#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == "":
        print("")
    else:
        for row in matrix:
            a = 0
            for value in row:
                a = a + 1
                if a < len(row):
                    print("{:d}" .format(value), end=" ")
                else:
                    print("{:d}" .format(value))
