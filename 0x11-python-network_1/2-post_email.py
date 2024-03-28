#!/usr/bin/python3
"""
a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
displays the body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    import urllib.request
    from sys import argv
    import urllib.parse

    url = argv[1]
    email = {'email': argv[2]}
    data = urllib.parse.urlencode('vlaue').encode('ascii')

    with urllib.request.urlopen(url, data) as response:
        body = response.read()
        print(body.decode('utf-8'))
