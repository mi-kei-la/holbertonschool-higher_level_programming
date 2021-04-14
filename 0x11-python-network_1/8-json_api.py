#!/usr/bin/python3
""" This script takes in a letter and sends a POST request with it.
"""


if __name__ == '__main__':
    import requests
    from sys import argv
    import json

    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) < 2:
        query = ""
    else:
        query = argv[1]
    r = requests.post(url, data={'q': query})
    try:
        response = r.json()
        print("[{}] {}".format(response['id'], response['name']))

    except Exception as e:
        print('No result')
