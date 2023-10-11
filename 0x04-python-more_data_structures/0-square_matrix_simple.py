#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    else:
        sqr_matrix = []
        for row in matrix:
            sqr_matrix.append(list(map(lambda x: x**2, row)))
        return sqr_matrix
