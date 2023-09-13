#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary)
    list(map(lambda x: print("{}: {}".format(
        x, a_dictionary[x])), sorted_keys))
