#!/usr/bin/python3
for i in range(0, 10):
    j = i + 1
    for j in range(j, 10):
        if i < 8:
            print("{}{}, " .format(i, j), end='')
        else:
            print("{}{}" .format(i, j))
