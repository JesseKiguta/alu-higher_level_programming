#!/usr/bin/python3
''' Dividing all the elements in a matrix '''


def matrix_divided(matrix, div):
    ''' Checks if div is a non-zero number '''

    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    ''' Checks if matrix is a list of lists with float/int '''

    if not all(isinstance(row, list) and all(isinstance(item, (int, float))
        for item in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)
        of integers/floats")

    ''' Checks if all rows have the same length '''

    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    ''' Divides all elements by div rounded to 2dp '''

    result_matrix = [[round(item / div, 2) for item in row] for row in matrix]

    return result_matrix
