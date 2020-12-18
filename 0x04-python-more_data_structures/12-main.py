#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
print("this should be 10")

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
print("this should be 7")

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
print("this should be 9")

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
print("this should be 87")

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
print("this should be 707")
