#!/usr/bin/python3
# sends a request to the URL and displays the value of the X-Request-Id
# variable found in the header of the response.
mport urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(t
