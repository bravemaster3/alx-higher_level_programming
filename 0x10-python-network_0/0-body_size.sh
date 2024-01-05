#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response

#Extract the headers
headers=$(curl -I -s "$1")

# Extract the content length
echo "$headers" | grep -i "Content-Length" | awk '{print $2}'
