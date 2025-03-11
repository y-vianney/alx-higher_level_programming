#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """
    Function that prints an integer
    Returns True if value has been correctly printed (it means the value is an integer)
    Otherwise, returns False and prints in stderr the error precede by Exception:
    """
    output = True

    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        output = False

    return output
