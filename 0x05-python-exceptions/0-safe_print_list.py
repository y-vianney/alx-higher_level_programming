#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """safe_print_list(my_list, x):
    Prints x elements of a list (my_list) and returns
    the real number of elements printed.
    """
    index = 0
    res = ""

    while True:
        try:
            if index == x:
                break
            res += str(my_list[index])
            index += 1
        except IndexError:
            break

    print(int(res) if res != "" else "")
    return index

