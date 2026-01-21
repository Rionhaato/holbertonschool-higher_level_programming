#!/usr/bin/python3


def no_c(my_string):
    chars = []
    for ch in my_string:
        if ch != "c" and ch != "C":
            chars.append(ch)
    return "".join(chars)
