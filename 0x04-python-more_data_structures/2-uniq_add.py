#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Add all unique integers in a list (only once for each integer).
    """

    return sum([x for i, x in enumerate(my_list) if x not in my_list[:i:]])
