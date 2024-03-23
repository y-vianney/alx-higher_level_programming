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
            result = 0
            a = args[0]
            b = args[2]
            if args[1] == "+":
                print("{} {} {} = {}".format(a, args[1], b, add(a, b)))
            elif args[1] == "-":
                print("{} {} {} = {}".format(a, args[1], b, sub(a, b)))
            elif args[1] == "*":
                print("{} {} {} = {}".format(a, args[1], b, mul(a, b)))
            else:
                print("{} {} {} = {}".format(a, args[1], b, div(a, b)))
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1);
