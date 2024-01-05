#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -iX OPTIONS "$1" | grep -i "Allow" | awk '{print $2}'
