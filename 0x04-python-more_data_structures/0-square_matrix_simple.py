#!/usr/bin/python3
"""
Module for square_matrix
"""


def square_matrix_simple(matrix=[]):
    return list(map(lambda x: list(map(lambda y: y ** 2, x)), matrix))
