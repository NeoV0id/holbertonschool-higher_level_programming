#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

print("Last digit of {}".format(number), end="")
if number >= 0:
    unit = number % 10
elif number < 0:
    num = number * -1
    unit = num % 10
    unit = unit * -1

if unit == 0:
    print(" is {} and is 0".format(unit))
elif unit < 6:
    print(" is {} and is less than 6 and not 0".format(unit))
elif unit > 5:
    print(" is {} and is greater than 5".format(unit))
elif number < 0:
    print(" is -{} and is less than 6 and not 0".format(unit))
