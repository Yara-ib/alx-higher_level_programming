#!/usr/bin/python3
""" Script sends request & get value of variable in response header """


if __name__ == '__main__':
    import requests
    from sys import argv

    request = requests.get(argv[1])
    print(request.headers.get('X-Request-Id'))
