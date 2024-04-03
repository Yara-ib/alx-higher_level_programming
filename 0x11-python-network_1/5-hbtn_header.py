#!/usr/bin/python3


if __name__ == '__main__':
    import requests
    from sys import argv

    request = requests.get(argv[1])
    print(request.headers.get('X-Request-Id'))
