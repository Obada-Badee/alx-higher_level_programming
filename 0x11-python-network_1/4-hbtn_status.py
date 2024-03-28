#!/usr/bin/python3
"""Fetch https://alx-intranet.hbtn.io/status using requests module"""


if __name__ == "__main__":
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    req = requests.get(url)
    print("Body response:")
    print(f"\t- type: {req.text.__class__}")
    print(f"\t- content: {req.text}")
