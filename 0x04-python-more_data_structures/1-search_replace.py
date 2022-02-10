#!/usr/bin/python3
"""
Module for search_replace
"""


def search_replace(my_list, search, replace):
    new = []
    for i in my_list:
        if (i == search):
            new.append(replace)
        else:
            new.append(i)
    return (new)
