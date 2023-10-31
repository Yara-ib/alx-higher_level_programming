#!/usr/bin/python3
for n in range(0, 10):
    for m in range(0, 10):
        if n >= m:
            continue
        elif n == 8 and m == 9:
            print("{n}{m}".format(n=n, m=m))
        else:
            print("{n}{m},".format(n=n, m=m), end=" ")
