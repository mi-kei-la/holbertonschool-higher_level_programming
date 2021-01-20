#!/usr/bin/python3
"""This is a single function module."""
import json
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


# Save arguments to new list.
args_list = argv[1:]

# Variable with the name of the json file to modify.
filename = "add_item.json"

# Try to open json file, and create new list with
# the contents of the file and the arguments list.
# If the file does not exist, it should be created,
# and arguments will be written.
try:
    jfile = load_from_json_file(filename)
    jlist = list(jfile)
    final_list = jlist + args_list
    save_to_json_file(final_list, filename)
except FileNotFoundError:
    save_to_json_file(args_list, filename)
