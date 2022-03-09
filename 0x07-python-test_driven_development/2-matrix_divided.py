#!/usr/bin/python3
""" Module for divide all elements of a matrix """

def matrix_divided(matrix, div):
    """
        function that divides all elements of a matrix.
            Args:
                matrix: matrix to divide
                div: int that divides the matrix
            Raises:
                TypeError: matrix must be int or float
                Each row of the matrix must have the same size if div is not of type int or float
            ZeroDivisionError: when div equal to 0
            Returns:
                new matrix
    """
    if not isinstance(matrix, (list, int, float)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for i in range(0, len(matrix)):
        a = []
        for j in matrix[i]:
            a.append(round((j / div), 2))
        new_matrix.append(a)
    return new_matrix
