#!/usr/bin/python3
j = 1
for i in range(122, 96, -1):
    k = i
    if j % 2 is 0:
        k = k - 32
    print("{}" .format(chr(k)), end='')
    j = j + 1
