#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import urllib.request
    my_url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(my_url)
    print("Body response:")
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")
