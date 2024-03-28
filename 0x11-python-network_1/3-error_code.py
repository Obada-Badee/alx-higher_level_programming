#!/usr/bin/python3
# Take in a URL, send a request to URL, and dispaly body


import sys
import urllib.request
from urllib.error import HTTPError

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as e:
        print(f'Error code: {e.code}')
