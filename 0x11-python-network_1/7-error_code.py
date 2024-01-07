#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays
the body of the response.
"""


if __name__ == "__main__":
    import requests
    import sys
    my_url = sys.argv[1]
    req = requests.get(my_url)
    if req.status_code != 200:
        print(f"Error code: {req.status_code}")
    else:
        print(req.text)
