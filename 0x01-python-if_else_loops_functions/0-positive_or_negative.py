#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    print("{:d} is negative" .format(number))
elif number == 0:
    print("{:d} is 0" .format(number))
else:
    print("{:d} is positive" .format(number))
