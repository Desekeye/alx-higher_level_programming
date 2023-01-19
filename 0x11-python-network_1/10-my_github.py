#!/usr/bin/python3
from requests.auth import HTTPBasicAuth
import sys


def searchapi():
    """status"""
    user = str(sys.argv[1])
    pat = str(sys.argv[2])
    result = requests.get("https://api.github.com/user",
                          auth=(HTTPBasicAuth(user, pat)))

    try:
        data = result.json()
        print(data["id"])
    except:
        print("None")

if __name__ == "__main__":
    searchapi()
