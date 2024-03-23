#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Return a set of all elements present in only one set.
    """

    return set(_ for _ in set_1 if _ not in set_2)
