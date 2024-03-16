#!/usr/bin/python3

for _ in range(122, 96, -1):
    letter = ""
    if _ % 2 == 0:
        letter = chr(_)
    else:
        letter = chr(_ - 32)
    print("{:s}".format(letter), end="")
