#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 123:
            i = ord(i) - 32
            i = chr(i)
        print("{}".format(i), end="")
    print(end="\n")
