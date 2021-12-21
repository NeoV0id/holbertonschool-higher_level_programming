#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    unit = number % 10
elif number < 0:
    num = number * -1
    unit = num % 10

if unit == 0:
    str = "and is 0"
elif unit < 6:
    str = "and is less than 6 and not 0"
elif unit > 5:
    str = "and is greater than 5"

if number > 0:
    print("Last digit of {} is {} {}".format(number, unit, str))

elif number < 0:
    print("Last digit of {} is -{} {}".format(number, unit, str))
