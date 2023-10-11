#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_tbd = []
    for k, v in a_dictionary.items():
        if v == value:
            keys_tbd.append(k)

    for key in keys_tbd:
        del a_dictionary[key]
    return a_dictionary
