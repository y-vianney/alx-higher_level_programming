#!/usr/bin/python3

def remove_char_at(str, n):
    str = list(str)

    if 0 <= n < len(str):
        str.pop(n)
    
    return ''.join(str)
