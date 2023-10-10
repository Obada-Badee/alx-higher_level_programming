#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or my_list == []:
        return None
    maxn = my_list[0]
    for i in my_list:
        if i > maxn:
            maxn = i
    return maxn
