#!/usr/bin/python3
""" Script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter """


if __name__ == '__main__':
    import requests
    from sys import argv

    value = {'email': argv[2]}
    new = requests.post(argv[1], data=value)
    print(new.text)
