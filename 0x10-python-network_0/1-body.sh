#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the body content of 200 OK
[ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" -eq 200 ]&& curl -s "$1"
