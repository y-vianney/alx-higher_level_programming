#!/usr/bin/python3

def max_integer(my_list=[]):
    maxi = None

    for num in my_list:
        if maxi is None or num > maxi:
            maxi = num

    return maxi
