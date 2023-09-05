#!/usr/bin/python3
def uppercase(str):
    for c in str:
        u = ord(c)
        U = chr(u - 97 + 65) if u > 96 and u < 123 else chr(u)
        print("{}".format(U), end='')
    print()
