#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """safe_print_list_integers(my_list=[], x=0) -> prints the first x elements
    of a list and only integers and returns the real number of integers printed
    """

    count = 0
    printed_count = 0

    while count < x:
        try:
            print("{:d}".format(my_list[count]), end="")
            printed_count += 1
        except Exception as e:
            if not isinstance(e, IndexError):
                pass
            else:
                raise e

        count += 1

    print()
    return printed_count
