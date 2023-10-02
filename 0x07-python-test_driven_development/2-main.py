#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

print("_______________")

print(matrix_divided([[8, 4.4], [8.8, 0]], 4))

print("_______________")

matrix = [
]
print(matrix_divided(matrix, 3))
print(matrix)
