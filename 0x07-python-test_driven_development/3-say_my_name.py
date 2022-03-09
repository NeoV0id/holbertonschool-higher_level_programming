#!/usr/bin/python3
""" Module for func say_my_name """


def say_my_name(first_name, last_name=""):
    """
        say_my_name will print names
        Args:
            first_name: first name
            last_name: last name
        Raises:
            TypeError: first_name and last_name must be string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
