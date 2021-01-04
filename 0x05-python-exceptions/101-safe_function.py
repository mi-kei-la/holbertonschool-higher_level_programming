#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    if __name__ != "main":
        try:
            result = fct(*args)
            return result
        except ZeroDivisionError:
            sys.stderr.write("Exception: division by 0\n")
        except IndexError:
            sys.stderr.write("Exception: list index out of range\n")
