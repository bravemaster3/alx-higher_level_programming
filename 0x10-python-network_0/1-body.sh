#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the body content of 200 OK
curl -sL "$1"
