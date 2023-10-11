#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        sqr_matrix = []
        for row in matrix:
            sq.append(list(map(lambda x: x**2, row)))
        print(sq)
