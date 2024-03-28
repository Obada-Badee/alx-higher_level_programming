#!/usr/bin/python3

"""
A python Script Fetch a url and display the value of
the X-Request-Id variable found
in the header of the response
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get(argv[1])
    xid = r.headers['X-Request-Id']
    print(xid)
