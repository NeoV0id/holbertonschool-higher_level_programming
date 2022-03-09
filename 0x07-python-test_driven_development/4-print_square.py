#!/usr/bin/python3
""" Module for print_square function """


def print_square(size):
    """
        print_square (will print square according to size)
        Args:
            size: size of square
        Raises:
            TypeError: size must be an int
            ValueError: size mustn't be inferior to 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(0, size):
            for j in range(0, size):
                print("#", end="")
            print()
