#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    elif roman_string == "":
        return 0
    num_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = num_d[roman_string[0]]
    for i in range(1, len(roman_string)):
        if num_d[roman_string[i - 1]] >= num_d[roman_string[i]]:
            number += num_d[roman_string[i]]
        else:
            number += num_d[roman_string[i]]
            number -= num_d[roman_string[i - 1]] * 2

    return number
