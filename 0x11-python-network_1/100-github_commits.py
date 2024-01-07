#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""


if __name__ == "__main__":
    import requests
    import sys
    user = sys.argv[1]
    repos = sys.argv[2]
    url = f"https://api.github.com/repos/{user}/{repos}/commits"
    response = requests.get(url, params={'per_page': 10})
    json_resp = response.json()
    for commit in json_resp:
        sha = commit["sha"]
        author_name = commit["commit"]["author"]["name"]
        print(f"{sha}: {author_name}")
