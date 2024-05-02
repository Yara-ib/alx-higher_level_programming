#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)"""


if __name__ == '__main__':
    from urllib import request, error
    from sys import argv

    try:
        url = request.Request(argv[1])
        with request.urlopen(url) as response:
            output = response.read().decode("utf-8")
            print(output)

    except error.HTTPError as e:
        print(f'Error code: {e.code}')
