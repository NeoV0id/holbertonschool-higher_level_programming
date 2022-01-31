#!/usr/bin/python3
"""
MyList module

"""


class MyList(list):
    """
    MyList class that inherits from List

    """
    def print_sorted(self):
        """
        Prints list

        """
        print(sorted(self))
