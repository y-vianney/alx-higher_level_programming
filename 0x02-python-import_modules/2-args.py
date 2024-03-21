#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) == 0:
        print("0 arguments.")
    else:
        if len(args) == 1:
            print("1 argument", end="")
        else:
            print("{} arguments".format(len(args)), end="")
        print(":")

        for index, _ in enumerate(args):
            print("{:d}: {}".format(index + 1, _))
