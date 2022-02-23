#!/usr/bin/python3

def weight_average(my_list=[]):
    result = 0
    tmp = []
    n = 0
    if my_list == None:
        return 0
    for i in my_list:
        result += my_list[0] * my_list[1]
        tmp.append(my_list[1])
    for j in tmp:
        n += tmp
    result = result / n