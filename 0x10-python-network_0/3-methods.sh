#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -I -X OPTIONS "$1" -o /dev/null | grep "Allow" | awk -F ": " '{print $2}'
