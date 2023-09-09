#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(-1, -len(my_list) - 1, -1):
        if isinstance(my_list[i], list):
            print_reversed_list_integer(my_list[i])
        else:
            print("{:d}".format(my_list[i]))
