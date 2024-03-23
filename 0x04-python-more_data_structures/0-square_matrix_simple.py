#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    A function that computes the square value of all integers of a matrix.
    """

    def square(x):
        return x*x

    return list(map(lambda row: list(map(square, row)), matrix))
