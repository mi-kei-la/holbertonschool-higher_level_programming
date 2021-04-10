#!/usr/bin/python3
""" This script takes an URL and sends a POST request with an email
as parameter, then displays the body of the response.
"""


if __name__ == "__main__":
    from urllib import parse, request
    from sys import argv

    query = {'email': argv[2]}
    encoded_args = parse.urlencode(query).encode('utf-8')
    with request.urlopen(argv[1], encoded_args) as response:
        page = response.read().decode('utf-8')
        print(page)
