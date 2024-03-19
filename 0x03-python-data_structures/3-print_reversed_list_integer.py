#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for _ in my_list[::-1]:
        print('{}'.format(_))

print_reversed_list_integer([1, 2, 3, 4, 5])
