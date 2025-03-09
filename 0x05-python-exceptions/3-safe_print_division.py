#!/bin/python3

def safe_print_division(a, b):
    """function that divides 2 integers and prints result.
    safe_print_division(a, b) -> Divides a by b, return the
    result, otherwise None
    """

    output = None

    try:
        output = a / b
    except Exception:
        pass
    finally:
        print("{}".format(output))
        return output
