#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, 
 and displays the body of the response (decoded in utf-8) """
import urllib.request
import urllib.parse
import sys


def sender():
    """sender"""
    v = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(v)
    data = data.encode("ascii")
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode("utf-8"))

if __name__ == "__main__":
    sender()
