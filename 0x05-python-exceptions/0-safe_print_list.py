#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed = 0
    try:
        for item in my_list[:x]:
            print(item, end="")
            printed += 1
        print()
    except TypeError:
        pass
    finally:
        return printed
