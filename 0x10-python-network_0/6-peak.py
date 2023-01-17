#!/usr/bin/python3
"""find_peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers."""
    if (not list_of_integers) or len(list_of_integers) == 0:
        return None
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        peak = list_of_integers[0]
        return peak
