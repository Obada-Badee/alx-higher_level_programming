#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            newchar = chr(ord(char) - 32)
        else:
            newchar = char

        print("{}".format(newchar), end="")
    print()
