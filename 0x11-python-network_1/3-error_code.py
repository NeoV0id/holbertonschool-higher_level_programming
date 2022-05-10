#!/usr/bin/python3
""" Module for task 3 """

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8", "replace"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
