#!/usr/bin/python3

def uppercase(str):
    return ' '.join([chr(ord(_) - 32) for _ in str.split(' ')])
