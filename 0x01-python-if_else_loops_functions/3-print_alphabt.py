#!/usr/bin/python3

alphabet = ""
for i in range(97, 123):
    if i not in [101, 113]:
        alphabet += chr(i)

print('{}'.format(alphabet))
