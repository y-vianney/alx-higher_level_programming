#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """safe_print_list_integers(my_list=[], x=0) -> prints the first x elements of
    a list and only integers and returns the real number of integers printed
    """

    count = 0
    printed_count = 0
    printed = ""

    while count < x:
        if isinstance(my_list[count], int):
            try:
                printed += str(my_list[count])
                printed_count += 1
            except IndexError:
                break

        count += 1

    print("{:d}".format(int(printed) if printed != "" else ""))
    return printed_count
