#!/usr/bin/python3
""" This script fetches an URL and handles errors.
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.get(argv[1])
    if r.status_code < 400:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
