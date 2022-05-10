#!/usr/bin/python3
""" Module for task 6 """

if __name__ == "__main__":
    import requests
    import sys

    req = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(req.text)
