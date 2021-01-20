#!/usr/bin/python3
"""This is a single function module."""
import json
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def is_file_empty(file_name):
    """ Check if file is empty by reading first character in it"""
    # open file in read mode
    with open(file_name, 'a+') as read_obj:
        # read first character
        one_char = read_obj.read(1)
        # if not fetched then file is empty
        if not one_char:
            print("File is empty")
            return True
    print("File is not empty")
    return False

filename = "add_item.json"
dumplist = list(argv)
dumplist.pop(0)
print(dumplist)
if is_file_empty(filename):
    save_to_json_file(dumplist, filename)
    is_file_empty(filename)
