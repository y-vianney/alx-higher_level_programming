#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    index = 0

    while True:
        try:
            print(elt[index])
            index += 1
            if (index + 1 == x):
                break
        except IndexError:
            print('')

    return index + 1
