#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for _ in my_list:
        print("{:d}".format(_))

print_list_integer([1, 2, 3, 4, 5])
