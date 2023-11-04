#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = my_list.copy()
    # if len(my_list) == len(list_result):
        # for num in my_list:
        #     if num % 2 == 0:
        #         return True
    # list_result =
    for idx in range(len(my_list)):
        # list_result[idx] += my_list[idx]
        if list_result[idx] % 2 == 0:
            return list_result[idx]
