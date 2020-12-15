#!/usr/bin/env python3
def no_c(my_string):
    if (my_string):
        new = ""
        for x in my_string:
            if x != "C" and x != "c":
                new = new + x
    return new
