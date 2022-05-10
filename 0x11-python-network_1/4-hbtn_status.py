#!/usr/bin/python3
""" Module for task 4 """

if __name__ == "__main__":
    import requests

    req = requests.get('https://intranet.hbtn.io/status')

    print('Body response:')
    print('\t- type: {}'.format(type(req.text)))
    print('\t- content: {}'.format(req.text))
