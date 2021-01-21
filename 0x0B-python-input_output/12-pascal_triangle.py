#!/usr/bin/python3
"""Pascal's triangle."""


def pascal_triangle(n):
    """Returns a list of lists, unless n is less or equal than 0."""
    ret = []
    if n <= 0:
        return ret
    if n >= 1:
        ret.append([1])
    if n >= 2:
        ret.append([1, 1])
    if n > 2:
        for i in range(2, n):
            lastlist = ret[i - 1]
            newlist = []
            newlist.append(lastlist[0])
            for j in range(len(lastlist) - 1):
                x = lastlist[j] + lastlist[j + 1]
                newlist.append(x)
            newlist.append(lastlist[len(lastlist) - 1])
            ret.append(newlist)
    return ret
