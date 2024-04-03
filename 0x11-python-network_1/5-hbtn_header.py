#!/usr/bin/python3
""" Script sends a request to URL & displays value of variable in response header """


if __name__ == '__main__':
    import requests
    from sys import argv

    try:
        request = requests.get(argv[1])
        print(request.headers.get('X-Request-Id'))

    except Exception as e:
        pass
