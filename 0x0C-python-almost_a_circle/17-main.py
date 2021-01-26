#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle
from models.square import Square
import io
from contextlib import redirect_stdout

if __name__ == "__main__":

    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)

    s1 = Square(3, 5)
    s1_dictionary = s1.to_dictionary()
    s2 = Square.create(**s1_dictionary)
    print(s1)
    print(s2)
    print(s1 is s2)
    print(s1 == s2)

    inst_pr = Rectangle(2, 3, 0, 0)
    inst_pr.display()
    printing = io.StringIO()
    with redirect_stdout(printing):
        inst_pr.display()
    printed = printing.getvalue()
    ideal_str = "##\n##\n##\n"
    print(ideal_str == printed)
