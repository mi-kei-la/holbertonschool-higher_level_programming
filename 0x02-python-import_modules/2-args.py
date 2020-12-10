#!/usr/bin/python3
import sys
if __name__ == "__main__":
    l = len(sys.argv)
    if l > 1:
        print("{} arguments:" .format(l - 1))
        count = 0
        for a in sys.argv:
            if count >= 1:
                print("{:d}: {:s}" .format(count, sys.argv[count]))
            count = count + 1
    else:
        print("0 arguments.")
