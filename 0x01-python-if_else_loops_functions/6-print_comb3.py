#!/usr/bin/python3
for i in range(0, 9):
    for j in range(1, 10):
        if j + i > 9:
            continue
        elif i == 0 and j == 9:
            print("{}{}".format(i, j), end=", ")
        elif i != 8 and j != 9:
            print("{}{}".format(i, j + i), end=", ")
print("{}".format(89))
