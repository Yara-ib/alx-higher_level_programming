#!/usr/bin/python3
""" Script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8) """


if __name__ == '__main__':
    from urllib import request, parse
    from sys import argv

    params = {'email': argv[2]}
    data = parse.urlencode(params).encode('ascii')
    with request.urlopen(argv[1], data) as response:
        print(response.read().decode("utf-8"))
