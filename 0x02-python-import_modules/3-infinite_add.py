#!/usr/bin/python3
import sys
x = 0
for i in range(1, len(sys.argv)):
    x = x + int(sys.argv[i])
print(x)
