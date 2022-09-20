#!/usr/bin/python3
def uppercase(str):
    uppercase = 0
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            uppercase = 32
        else:
            uppercase = 0
        print("{:c}".format(ord(char) - uppercase), end='')
    print()
