#!/usr/bin/python3
""" This module takes in an URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""


if __name__ == '__main__':
    from sys import argv
    from urllib import request

    with request.urlopen(argv[1]) as response:
        request_id = response.info().get("X-Request-Id")
        print(request_id)
