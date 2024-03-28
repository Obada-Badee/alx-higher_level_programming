#!/usr/bin/python3
"""
a Python script that:
    takes in a URL
    sends a request to the URL
    displays the value of the X-Request-Id variable
"""

if __name__=="__main__":
    import urllib.request
    from sys import argv

    with urllib.request.urlopen(argv[1]) as response:
        print(response.headers['X-Request-Id'])
