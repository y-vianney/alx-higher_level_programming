#!/usr/bin/python3

def remove_char_at(str, n):
    str = list(str)

    if n < 0:
        n *= -1

    if n < len(str) - 1:
        str.pop(n)
    
    return ''.join(str)
