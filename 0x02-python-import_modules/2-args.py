#!/usr/bin/python3
import sys
if __name__ == "__main__":
    l = len(sys.argv) - 1
    if l == 1:
        print("{} argument:" .format(l))
        print("{:d}: {:s}" .format(l, sys.argv[l]))
    elif l > 1:
        print("{} arguments:" .format(l))
        count = 1
        for a in sys.argv:
            print("{:d}: {:s}" .format(count, sys.argv[l]))
            count = count + 1
    else:
        print("0 arguments.")
