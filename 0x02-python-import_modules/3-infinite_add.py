#!/usr/bin/python3
import sys

if __name__ == '__main__':
    n = 0
    for i in sys.argv[1:]:
        n += int(i)
    print("{}".format(n))
