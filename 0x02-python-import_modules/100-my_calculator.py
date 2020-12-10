#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    avlen = len(argv)

    if avlen != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    sign = str(argv[2])
    if sign != '+' and sign != '-' and sign != '/' and sign != '\*':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if sign == '+':
        print("{} + {} = {}" .format(a, b, add(a, b)))

    elif sign == '-':
        print("{} - {} = {}" .format(a, b, sub(a, b)))

    elif sign == '*':
        print("{} * {} = {}" .format(a, b, mul(a, b)))

    elif sign == '/':
        print("{} / {} = {}" .format(a, b, sub(a, b)))
