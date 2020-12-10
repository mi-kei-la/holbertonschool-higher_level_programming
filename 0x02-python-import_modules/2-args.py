#!/usr/bin/python3
import sys
if __name__ == "__main__":
    l = len(sys.argv)
    if l is 1:
        print("0 arguments.")
    elif l is 2:
        count = 1
        print("{} argument:" .format(l - 1))
        print("{:d}: {:s}" .format(count, sys.argv[count]))
    elif l > 2:
        print("{} arguments:" .format(l))
        count = 0
        for a in sys.argv:
            if count >= 1:
                print("{:d}: {:s}" .format(count, sys.argv[count]))
            count = count + 1
