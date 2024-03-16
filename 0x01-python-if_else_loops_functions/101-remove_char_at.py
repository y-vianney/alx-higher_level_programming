#!/usr/bin/python3

def remove_char_at(str, n):
    str = list(str)

    if abs(n) < len(str) - 1:
        str.pop(abs(n))
    
    return ''.join(str)
