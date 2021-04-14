#!/usr/bin/python3
""" This script takes in an URL and displays the value of a header.
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
