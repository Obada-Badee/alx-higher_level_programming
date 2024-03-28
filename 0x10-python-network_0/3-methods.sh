#!/bin/bash
# a Bash script that takes in a URL and displays all HTTP methods
curl -sILX OPTIONS "$1" | grep Allow
