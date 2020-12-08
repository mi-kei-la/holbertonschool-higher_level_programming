#!/usr/bin/python3
def uppercase(str):
    for x in str:
        x = ord(x)
        if x >= 97 and x <= 122:
            x = x - 32
        print("{}" .format(chr(x)), end='')
    print("")
