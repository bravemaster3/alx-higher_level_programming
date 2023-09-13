#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_cpy = a_dictionary.copy()
    for k in a_cpy.keys():
        if a_dictionary[k] == value:
            a_dictionary.pop(k)
    return (a_dictionary)
