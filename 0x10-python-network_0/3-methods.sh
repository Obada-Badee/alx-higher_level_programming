#!/bin/bash
# a Bash script that takes in a URL and displays all HTTP methods
curl -sIX OPTIONS "$1" | grep Allow | cut -d ' ' -f2-
