#!/usr/bin/python3
import sys
""" Log parsing Module. """


total_size = 0
count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
n_line = 0

try:
    with open("file.txt", "a+") as file:
        file.read()
        for line in sys.stdin:
            try:
                args = line.split()
                status_code = int(args[-2])
                file_size = int(args[-1])

                total_size += file_size

                if status_code in count:
                    count[status_code] += 1

            except (ValueError, IndexError):
                pass

            n_line += 1

            if n_line % 10 == 0:
                print(f"Total file size: {total_size}")
                for code, code_count in sorted(count.items()):
                    if code_count > 0:
                        print(f"{code}: {code_count}")

except KeyboardInterrupt:
    print(f"Total file size: {total_size}")
    for code, code_count in sorted(count.items()):
        if code_count > 0:
            print(f"{code}: {code_count}")
