#!/usr/bin/python3
""" This script takes in an URL and displays the body of response.
"""


if __name__ == '__main__':
    from sys import argv
    from urllib import request, error

    try:
        with request.urlopen(argv[1]) as response:
            page = response.read().decode('utf-8')
            print(page)
    except error.HTTPError as error:
        print('Error code: {}'.format(error.code))
