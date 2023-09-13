#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_cpy = a_dictionary.copy()
    list(map(lambda x: a_cpy.update({x: 2 * a_cpy[x]}), a_cpy.keys()))
    return (a_cpy)
