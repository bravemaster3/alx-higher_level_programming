#!/usr/bin/python3
"""
This module contains a function for multiplying two matrices
"""


def matrix_mul(m_a, m_b):
    """content of the actual function"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if len(m_a) > 0:
        for elem in m_a:
            if type(elem) is not list:
                raise TypeError("m_a must be a list of lists")
    if len(m_b) > 0:
        for elem in m_b:
            if type(elem) is not list:
                raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for elem in m_a:
        for el in elem:
            if type(el) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")

    for elem in m_b:
        for el in elem:
            if type(el) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    height_a = len(m_a)
    height_b = len(m_b)
    width_a = len(m_a[0])
    width_b = len(m_b[0])
    for elem in m_a:
        if len(elem) != width_a:
            raise TypeError("each row of m_a must be of the same size")
    for elem in m_b:
        if len(elem) != width_b:
            raise TypeError("each row of m_b must be of the same size")

    if width_a != height_b:
        raise ValueError("m_a and m_b can't be multiplied")

    product = [[0 for _ in range(width_b)] for _ in range(height_a)]
    for i in range(height_a):
        for j in range(width_a):
            product[i][j] = sum(m_a[i][k] * m_b[k][j] for k in range(width_a))
    return product
