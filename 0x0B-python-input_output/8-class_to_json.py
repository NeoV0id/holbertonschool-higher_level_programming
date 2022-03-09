#!/usr/bin/python3
"""
class_to_json module
"""


def class_to_json(obj):
    """
    Dictionnary description via JSON
    """
    return(obj.__dict__)