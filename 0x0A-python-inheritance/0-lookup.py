#!/usr/bin/python3
"""
Lookup Module

"""


def lookup(obj):
    
    """
    Function that returns the list of attributes and methods of objects

    Args:
        obj: object to check

    Returns:
         list of available attributes and methods of an object
    """
    return dir(obj)
