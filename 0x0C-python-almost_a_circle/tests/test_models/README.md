# 0x0C. Python - Almost a circle

This repository contains all unit test files pertaining the 0x0C - Python project of the holberton School foundations programme.

## test_base tests:

- creation
- id and automatic increase

*Methods:*
- to_json_string
    - empty values
    - type of return
    - subclasses
- to_dictionary
- create
- load_from_file
- save_to_file
- save_to_file_csv

## test_rectangle tests:

*Type of arguments (testing all values):*

- negatives
- strings
- floats (regular float, infinity float, NaN float)
- booleans
- None
- 0 (for width and height)
- Less and more arguments than expected

*Methods:*
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

## test_square tests:

- Type of arguments
- Number of arguments
- Invalid values

*Methods:*
- area
- update
- display
