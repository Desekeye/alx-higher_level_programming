#!/usr/bin/python3
"""
add_integer
A function that adds 2 integers
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b
    Raise: TypeError
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
