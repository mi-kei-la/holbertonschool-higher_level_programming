#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    avlen = len(sys.argv)

    if avlen != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    sign = str(sys.argv[2])
    if sign != '+' and sign != '-' and sign != '/' and sign != '\*':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sign == '+':
        print("{} + {} = {}" .format(a, b, add(a, b)))
        exit(0)
    elif sign == '-':
        print("{} - {} = {}" .format(a, b, sub(a, b)))
        exit(0)
    elif sign == '*':
        print("{} * {} = {}" .format(a, b, mul(a, b)))
        exit(0)
    elif sign == '/':
        print("{} / {} = {}" .format(a, b, sub(a, b)))
        exit(0)
