#!/bin/bash
# a Bash script that takes in a URL and displays all HTTP methods
curl -sIX OPTIONS 0.0.0.0:5000/route_4 | grep Allow | cut -d ' ' -f2-
