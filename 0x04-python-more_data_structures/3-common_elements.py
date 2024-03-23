#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Return a set of common elements in two sets.
    """

    return set(_ for _ in set_1 if _ in set_2)
