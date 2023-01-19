#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays the body of the response"""
import requests
import sys


def errorcode():
    """status"""
    result = requests.get(sys.argv[1])
    try:
        if result.status_code > 400:
            print("Error code: {}".format(result.status_code))
        else:
            print(result.content.decode("utf-8"))
    except KeyError:
        pass

if __name__ == "__main__":
    errorcode()
