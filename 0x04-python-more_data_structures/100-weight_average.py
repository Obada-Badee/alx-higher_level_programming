#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    tscore, tweight = 0, 0
    for t in my_list:
        tscore += t[0] * t[1]
        tweight += t[1]
    return tscore / tweight
