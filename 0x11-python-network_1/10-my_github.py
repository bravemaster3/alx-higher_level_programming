#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""


if __name__ == "__main__":
    import requests
    import sys
    my_url = "https://api.github.com/user"
    user = sys.argv[1]
    passwd = sys.argv[2]
    response = requests.get(my_url, auth=(user, passwd))
    if 'id' in response.json():
        print(response.json()['id'])
    else:
        print(None)
