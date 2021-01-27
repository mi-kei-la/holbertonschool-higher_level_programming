# 0x0C. Python - Almost a circle

This repository contains all files pertaining the 0x0C - Python project of the holberton School foundations programme.

The */models* directory contains all files pertaining the creation of classes and it's attributes, while the directory tests contains all unit tests for said classes and methods.

## Base

Base class is the parent class of Rectangle. It creates and validates ID, and contains the following methods:

- to_json_string
    - empty values
    - type of return
    - subclasses
- to_dictionary
- create
- load_from_file
- save_to_file
- save_to_file_csv

## Rectangle:

Rectangle class creates an object of type Rectangle. At the moment of creation it takes width, height, x and y attributes. Width and height must be integers over 0, x and y over or equal to 0.

It contains the following methods:
- area()
- str()
- to_dictionary()
- update() with:
    - valid arguments
    - valid key-value arguments
    - valid arguments and key-value arguments
    - invalid data types
    - too many parameters
- display()

## Square:

Class Square inherits from the class rectangle, but size is both width and height.

It contains the following methods:
- area
- update
- display
