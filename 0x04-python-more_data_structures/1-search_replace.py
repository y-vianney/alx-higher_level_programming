#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replace  all occurrences of an element by another in a new list.
    """

    return [_ if _ != search else replace for _ in my_list]
