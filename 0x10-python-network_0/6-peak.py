#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers """

def find_peak(list_of_integers):
    """
        find_peak: function that finds a peak in a list of unsorted integers
        args:
            list_of_integers (list): list of unsorted integers
    """
    tmp = 0
    for i in range(0, len(list_of_integers)):
        if list_of_integers[i] > list_of_integers[i+1]:
            tmp = list_of_integers[i]
    return tmp
