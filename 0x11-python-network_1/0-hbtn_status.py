#!/usr/bin/python3
"""  Python script that fetches https://alx-intranet.hbtn.io/status """


if __name__ == '__main__':
    from urllib import request

    with request.urlopen('https://alx-intranet.hbtn.io/status') as url:
        readable = url.read()
        print(f'Body response:\n\t- type: {type(readable)}')
        print(f'\t- content: {readable}')
        print(f'\t- utf8 content: {readable.decode("utf-8")}')
