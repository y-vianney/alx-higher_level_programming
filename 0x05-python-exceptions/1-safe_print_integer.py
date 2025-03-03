#!/usr/bin/python3

def safe_print_integer(value):
    """safe_print_integer(value) -> prints an integer with "{:d}".format()
    and returns True if value has been correctly printed
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        pass

    return False
