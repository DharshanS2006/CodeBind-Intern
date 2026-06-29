import numpy as np


numbers = np.array([10, 20, 30, 40, 50, 60])
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Original 1D Array:")
print(numbers)

print("\nReversed 1D Array:")
print(numbers[::-1])

print("\nOriginal 2D Array:")
print(matrix)

print("\nReverse Rows:")
print(matrix[::-1])

print("\nReverse Columns:")
print(matrix[:, ::-1])

print("\nReverse Rows and Columns:")
print(matrix[::-1, ::-1])
