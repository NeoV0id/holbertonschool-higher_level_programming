#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    else:
        for i in range(0, len(str)):
            if i == n:
                i = ''
    return str
