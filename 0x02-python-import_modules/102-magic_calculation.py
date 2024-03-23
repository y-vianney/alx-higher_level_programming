#!/usr/bin/python3

from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    """
    Performs magic calculation based on a and b values.
    This function mimics the behavior of the provided bytecode.

    Parameters:
    a (int): The first operand.
    b (int): The second operand.

    Returns:
    int: The result of the magic calculation.
    """

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    return sub(a, b)
