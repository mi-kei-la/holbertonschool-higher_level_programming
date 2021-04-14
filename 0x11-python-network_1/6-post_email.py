#!/usr/bin/python3
""" This script makes a POST request with an email to a website.
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
