#!/usr/bin/python3
def roman_to_int(roman_string):
    lookup = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    if not isinstance(roman_string, str) or roman_string == None:
        return 0
    lst = list(roman_string)
    repl = list(map(lambda x: lookup[x], lst))
    if len(repl) >= 2:
        for i in range(len(repl) - 1):
            if (repl[i] < repl[i+1]):
                repl[i+1] = repl[i+1] - repl[i]
                repl[i] = 0

    return sum(repl)
