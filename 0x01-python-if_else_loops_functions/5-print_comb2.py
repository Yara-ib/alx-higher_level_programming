#!/usr/bin/python3
for number in range(0, 100):
    if number == 99:
        print("{number:02}".format(number=number))
        break
    print("{number:02},".format(number=number), end=" ")
