#!/usr/bin/python3
def pow(a, b):
    if a < 0:
        a = a * -1
        result = a ** b
        result = result * -1
    else:
        result = a ** b

    return result
