#!/usr/bin/python3
""" script that takes in a URL and an email address, ..."""
import requests
import sys


def post():
    """status"""
    result = requests.post(sys.argv[1], data={"email": sys.argv[2]})

    print(result.text)

if __name__ == "__main__":
    post()
