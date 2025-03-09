#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """safe_print_list_integers(my_list=[], x=0) -> prints the first x elements
    of a list and only integers and returns the real number of integers printed
    """

    count = 0
    printed_count = 0

    while count < x:
        if isinstance(my_list[count], int):
            print("{:d}".format(my_list[count]), end="")
            printed_count += 1

        count += 1

    print()
    return printed_count
