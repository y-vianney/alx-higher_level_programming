#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for _ in row:
            if list(row).index(_) == len(row) - 1:
                print('{}'.format(_), end="")
            else:
                print('{}'.format(_), end=" ")
        print('$')
