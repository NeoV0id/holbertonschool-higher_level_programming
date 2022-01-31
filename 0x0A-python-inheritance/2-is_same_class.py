#!/usr/bin/python3

""" 
is_same_class Module 

"""


def is_same_class(obj, a_class):

    """
    Function that check if objects is an instance of a class
    Args:
        obj (object): object to check
        a_class (class): class to check
    Returns:
        True: if object is an instance of the class
        False: if not
    """

    if type(obj) == a_class:
        return True
    else:
        return False
