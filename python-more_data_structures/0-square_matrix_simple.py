#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for row in matrix:
        square_row = [num ** 2 for num in row]
        square_matrix.append(square_row)
    return square_matrix
