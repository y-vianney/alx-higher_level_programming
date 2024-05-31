#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for elt in my_list:
            print(elt)
        print('\n')
    except IndexError:
        print('')

