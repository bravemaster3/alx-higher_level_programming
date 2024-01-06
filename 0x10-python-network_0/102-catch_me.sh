#!/bin/bash
# Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -sLX PUT 0.0.0.0:5000/catch_me_2 -d "user_id=98" -H "Origin: School"
