#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list != []:
        for num in range(len(my_list)):
            if my_list[num] > my_list[len(my_list) - 1]:
                max = my_list[num]
        return max
