#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        x = 0
        for y in my_list:
            if y > x:
                x = y
        return x
    else:
        return None
