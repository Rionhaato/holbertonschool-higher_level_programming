#!/usr/bin/python3


def uppercase(str):
    result = ""
    for ch in str:
        code = ord(ch)
        if ord('a') <= code <= ord('z'):
            result += chr(code - 32)
        else:
            result += ch
    print("{}".format(result))
