#!/usr/bin/python3
""" module for class square """


class Square:
    """ Square: define a square
        Attributes:
            width (int): size (height and width) of the square
    """
    def __init__(self, size):
        """ __init__ : initialisation of Square class
        Args:
            size (int): size (height and width) of the square
        """
        self.__size = size
