def uppercase(str):

    for i in str:

        if chr(i) > 97 and chr(i) < 123:
            i = ord(i) - 32
        else:
            pass

print("{}".format(chr(i)))
