#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_int = 0
    if type(roman_string) != str:
        return 0
    for i in roman_string:
        if i == "I":
            roman_int += 1
        elif i == "V":
            if i-1 == "I":
                roman_int += 4
            else:
                roman_int += 5
        elif i == "X":
            roman_int += 10
        elif i == "L":
            if i-1 == "X":
                roman_int += 40
            else:
                roman_int += 50
        elif i == "C":
            roman_int += 100
        elif i == "D":
            if i-1 == "C":
                roman_int += 400
            else:
                roman_int += 500
        elif i == "M":
            if i-1 == "C":
                roman_int += 900
            else:
                roman_int += 1000
    return roman_int