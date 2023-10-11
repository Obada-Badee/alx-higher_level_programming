#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    else:
        sqr_matrix = []
        for row in matrix:
            sqr_matrix.append(list(map(lambda x: x**2, row)))
        return sqr_matrix
