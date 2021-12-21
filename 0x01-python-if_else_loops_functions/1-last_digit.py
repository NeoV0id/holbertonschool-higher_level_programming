#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
unit = number % 10

if unit == 0:
    str = "and is 0"
elif unit > 5:
    str = "and is greater than 5"
else:
    str = "and is less than 6 and not 0"

print("Last digit of {:d} is {:d} {}".format(number, unit, str))
