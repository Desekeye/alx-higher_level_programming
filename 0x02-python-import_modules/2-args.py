#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    num = len(sys.argv) - 1
    if num == 0:
        print("{} arguments.".format(num))
    elif num == 1:
        print("{} argument:".format(num))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(num))
        for i in range(1, num + 1):
            print("{}: {}".format(i, sys.argv[i]))
