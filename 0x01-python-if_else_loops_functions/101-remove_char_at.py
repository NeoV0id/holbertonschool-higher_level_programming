#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    else:
        for i in str:
            if i == n:
                i = ''
            str += i
    return str
