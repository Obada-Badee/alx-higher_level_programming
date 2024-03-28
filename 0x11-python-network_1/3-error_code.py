#!/usr/bin/python3
"""
Take in a URL, send a request to URL, and dispaly body
"""


from sys import argv
import urllib.request
from urllib.error import HTTPError

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as e:
        print(f'Error code: {e.code}')
