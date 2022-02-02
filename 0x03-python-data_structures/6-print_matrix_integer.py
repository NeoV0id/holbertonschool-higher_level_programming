#!/usr/bin/python3
def print_matrix_integer(matrix[[]]):
    if type(matrix) is not list:
        return
    for i in matrix:
        if type(i) is not list:
            return
        for j in i:
            if type(j) is not integer:
                return
            elif j:
                print(j, end="")
            elif j != len(i)-1:
                print(" ")
        print()
