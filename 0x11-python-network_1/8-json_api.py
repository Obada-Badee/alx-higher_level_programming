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

    if (type(r_divt) is not dict):
        print('Not a valid JSON')
    elif (len(r_dict) > 0):
        print(f"[{r_dict['id']}] {r_dict['name']}")
    else:
        print("No result")
