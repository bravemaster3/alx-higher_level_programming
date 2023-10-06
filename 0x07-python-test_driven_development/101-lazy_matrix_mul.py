#!/usr/bin/python3

"""
Matrix multiplication using numpy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Lazy lazy boy"""
    arr1 = np.array(m_a)
    arr2 = np.array(m_b)
    result = np.multiply(arr1, arr2)
    return result.tolist()
