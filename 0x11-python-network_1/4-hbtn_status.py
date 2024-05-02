#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """


if __name__ == '__main__':
    import requests

    url = requests.get('https://alx-intranet.hbtn.io/status')
    print(f'Body response:\n\t- type: {type(url.content.decode("utf-8"))}')
    print(f'\t- content: {url.content.decode("utf-8")}')
