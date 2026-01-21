#!/usr/bin/python3


def max_integer(my_list=[]):
    if not my_list:
        return None
    max_val = my_list[0]
    for value in my_list[1:]:
        if value > max_val:
            max_val = value
    return max_val
