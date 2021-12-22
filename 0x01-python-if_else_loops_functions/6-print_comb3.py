#!/usr/bin/python3
for j in range(10):
    for i in range(10):
        if i > j:
            if j == 8:
               print("{:d}{:d}\n".format(j, i), end="")
            else:
                print("{:d}{:d}, ".format(j, i), end="")
        elif i == j:
            pass
        else:
            pass
