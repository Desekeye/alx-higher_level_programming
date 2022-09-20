#!/usr/bin/python3
""" 122 = 'z', 96 = '`' """
for num in range(122, 96, -1):
    if num % 2 == 0:
        print("{}".format(chr(num)), end='')
    else:
        print("{}".format(chr(num - 32)), end='')
