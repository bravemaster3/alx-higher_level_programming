#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = 0 if len(tuple_a) == 0 else list(tuple_a)[0]
    a2 = 0 if len(tuple_a) < 2 else list(tuple_a)[1]
    b1 = 0 if len(tuple_b) == 0 else list(tuple_b)[0]
    b2 = 0 if len(tuple_b) < 2 else list(tuple_b)[1]
    return (a1 + b1, a2 + b2)
