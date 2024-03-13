#!/usr/bin/python3

alphabet = ""
for i in range(97, 123):
    if i not in [101, 113]:
        alphabet += char(i)

print('{}'.format(alphabet))
