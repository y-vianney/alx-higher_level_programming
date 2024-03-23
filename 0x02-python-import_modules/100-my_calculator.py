#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]

    if len(args) == 3:
        if args[1] not in "-+/*":
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            print("{} {} {} = {}".format(args[0], args[1], args[2], eval(''.join(args))))
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1);
