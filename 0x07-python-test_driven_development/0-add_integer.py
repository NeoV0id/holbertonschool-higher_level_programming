#!/usr/bin/python3
""" Module for add integers """


def add_integer(a, b=98):
    """
        add_integers (effectuate addition
        Args:
            a: int
            b: int
        Raises:
            TypeError: a and b must be integers
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    elif type(a) is float:
        a = int(a)
    elif type(b) is float:
        b = int(b)
    return (a + b)
