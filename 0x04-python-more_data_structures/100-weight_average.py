#!/usr/bin/python3
def weight_average(my_list=[]):
    new = []
    l = len(my_list)
    x = my_list[0][0]
    for i in range(0, l):
        new.append(my_list[i][1])
        x = new[i] + x
    return x / l
