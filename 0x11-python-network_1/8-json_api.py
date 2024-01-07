#!/usr/bin/python3
"""
Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""


if __name__ == "__main__":
    import requests
    import sys
    my_url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    response = requests.post(my_url, data={'q': q})
    try:
        json = response.json()
        if json:
            print(f"[{json['id']}] {json['name']}")
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
