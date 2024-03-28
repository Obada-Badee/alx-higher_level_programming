#!/usr/bin/python3
"""
Python script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""


import requests
from sys import argv

if __name__ == '__main__':

    q = argv[1] if len(argv) == 2 else ""
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data={'q': q})
    r_dict = r.json()

    if (type(json) is dict):
        id, name = r_dict.get('id'), r_dict.get('name')
        if len(r_dict) == 0 or not id or not name:
            print("No result")
        else:
            print(f"[{r_dict.get('id')}] {r_dict.get('name')}")
    else:
        print("Not a valid JSON")
