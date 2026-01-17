#!/usr/bin/python3
for code in range(ord('a'), ord('z') + 1):
    if code != ord('q') and code != ord('e'):
        print("{:c}".format(code), end="")
