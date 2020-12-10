#!/usr/bin/python3
import sys
if __name__ == "__main__":
    l = len(sys.argv) - 1
    if l == 1:
        print("{} argument:" .format(l))
        print("{:d}: {:s}" .format(l, sys.argv[l]))
    elif l > 1:
        print("{} arguments:" .format(l))
        for a in range(1, len(sys.argv)):
            print("{:d}: {:s}" .format(a, sys.argv[a]))
    else:
        print("0 arguments.")
