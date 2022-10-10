#!/usr/bin/python3
def safe_print_division(a, b):
    d = 0
    try:
        d = a / b
    except (TypeError, ZeroDivisionError):
        d = none
    finally:
        print("Inside Result: {}".format(d))
        return d
