#!/usr/bin/python3

"""
Pascal Triangle constructor
"""


def pascal_triangle(n):
    """function definition"""
    if n <= 0:
        return []
    tri = []
    if n >= 1:
        tri.append([1])
    if n >= 2:
        tri.append([1, 1])
    if n > 2:
        for i in range(2, n):
            prev_row = tri[i - 1]
            curr_row = [1]
            for j in range(len(prev_row) - 1):
                elem1 = prev_row[j]
                elem2 = prev_row[j+1]
                curr_row.append(elem1 + elem2)
            curr_row.append(1)
            tri.append(curr_row)
    return tri
