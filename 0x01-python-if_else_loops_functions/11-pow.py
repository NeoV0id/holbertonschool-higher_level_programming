#!/usr/bin/python3
def pow(a, b):
    if a < 0:
        a = a * -1
        result = a ** b
        if a < b:
            result = result * -1
    elif a < 0 and b < 0:
        a = a * -1
        result = a ** b
    else:
        result = a ** b

    return result
