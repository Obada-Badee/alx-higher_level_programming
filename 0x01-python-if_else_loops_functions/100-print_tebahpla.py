#!/usr/bin/python3
for i in range(25, 0, -2):
    print("{}{}".format(chr(97 + i), chr(65 + i - 1)), end="")
