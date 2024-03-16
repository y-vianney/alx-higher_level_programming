#!/usr/bin/python3

print(''.join([chr(_) if _ % 2 == 0 else chr(_ - 32) for _ in range(122, 96, -1)]))
