#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    import urllib.request
    from urllib.error import URLError
    import sys
    my_url = sys.argv[1]
    req = urllib.request.Request(my_url)
    with urllib.request.urlopen(req) as response:
        try:
            print(response.read().decode('utf-8'))
        except URLError as e:
            print(f"Error code: {e.code}")
