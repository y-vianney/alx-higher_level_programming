#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = map(int, sys.argv[1:])

    print(sum(args))
