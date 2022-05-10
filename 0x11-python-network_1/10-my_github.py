#!/usr/bin/python3
""" Module for task 10 """

if __name__ == "__main__":
    import requests
    import sys

    req = requests.get('https://api.github.com/user',
                       auth=(sys.argv[1], sys.argv[2]))
    if req.status_code >= 400:
        print('None')
    else:
        print(req.json().get('id'))
