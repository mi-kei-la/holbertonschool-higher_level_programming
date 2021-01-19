#!/usr/bin/python3
"""This is a single class module.

MyList is a subclass of the class List.
"""


class MyList(list):
    """This class is inherited from the class list.

    Methods:
        print_sorted: prints the list items in ascending order.

    """
    def print_sorted(self):
        """Print int list in ascending order.

        Raises:
            ValueError: if list is empty.
        """
        if type(self) != MyList:
            raise TypeError("object must be a MyList")
        print(sorted(self))
