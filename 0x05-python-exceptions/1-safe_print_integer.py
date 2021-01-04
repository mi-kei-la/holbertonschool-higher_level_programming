#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
        return False
