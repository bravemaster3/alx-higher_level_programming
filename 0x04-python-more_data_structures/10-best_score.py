#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        a_sorted = sorted(a_dictionary.items(),
                          key=lambda x: x[1], reverse=True)
        return a_sorted[0][0]
    else:
        return None
