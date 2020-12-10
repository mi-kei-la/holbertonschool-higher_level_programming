#!/usr/bin/python3
from hidden_4 import *
if __name__ == "__main__":
    count = dir()
    for a in range(0, len(count)):
        if count[a][:1] != "_":
            print(count[a])
