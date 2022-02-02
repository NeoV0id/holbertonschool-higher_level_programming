#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0:
        pass
    else:
        for i in str:
            if i == n:
                i = ''
            str += i
