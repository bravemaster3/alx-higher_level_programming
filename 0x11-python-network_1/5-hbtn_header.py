#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""


if __name__ == "__main__":
    import requests
    import sys
    my_url = sys.argv[1]
    req = requests.get(my_url)
    header = req.headers['X-Request-Id']
    print(header)
