import numpy as np


numbers = np.array([1, 2, 3, 4, 5])

print("Original Array:")
print(numbers)

print("\nCumulative Sum:")
print(np.cumsum(numbers))

print("\nCumulative Product:")
print(np.cumprod(numbers))

print("\nDifference Between Consecutive Elements:")
print(np.diff(numbers))

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nOriginal Matrix:")
print(matrix)

print("\nRow-wise Cumulative Sum:")
print(np.cumsum(matrix, axis=1))

print("\nColumn-wise Cumulative Sum:")
print(np.cumsum(matrix, axis=0))
