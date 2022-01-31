#!/usr/bin/python3
""" 
inherits_from 

"""


def inherits_from(obj, a_class):
    """
    function to check if an object inherited from a class (instance)
    Args:
        obj (object): object to check
        a_class (class): class to check
    Returns:
        True:  if the object inherited from class (instance)
        False: otherwise
    """

    if issubclass(obj.__class__, a_class) and type(obj) != a_class:
        return True

    else:
        return False
