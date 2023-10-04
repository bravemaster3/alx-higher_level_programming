#!/usr/bin/python3
"""
This module contains a function for dividing a matrix
The matrix is a list of integers or floats, so is div
"""


def matrix_divided(matrix, div):
    """The matrix division function"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if len(matrix) == 0 or type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    height = len(matrix)
    width = len(matrix[0])
    for i in range(height):
        if type(matrix[i]) is not list or len(matrix[i]) == 0:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if len(matrix[i]) != width:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(width):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            if type(div) not in [int, float]:
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")

    return [[round(x/div, 2) for x in row] for row in matrix]
