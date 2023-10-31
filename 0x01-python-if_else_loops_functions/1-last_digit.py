#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_0 = str(number)
str1 = "Last digit of "
str2 = " and is greater than 5"
str3 = " and is less than 6 and not 0"
if str_0[-1] > 5:
    print(str1 + str_0, "is", str_0[-1] + str2)
elif str_0[-1] == 0:
    print(str1 + str_0, "is", str_0[-1], "and is 0")
else:
    print(str1 + str_0, "is", str_0[-1] + str3)
