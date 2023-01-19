#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password) and 
  uses the GitHub API to display your id """
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
