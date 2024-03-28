#!/usr/bin/python3
"""
Python script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    payload = {'q': ''}
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        payload['q'] = argv[1]
    r = requests.post(url, data=payload)
    json = r.json()
    if (type(json) is not dict):
        print('Not a valid JSON')
    elif (len(json) > 0):
        print(f"[{json['id']}] {json['name']}")
    else:
        print("No result")
