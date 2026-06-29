import numpy as np


matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("2D NumPy Array:")
print(matrix)

print("\nArray Information:")
print("Dimensions:", matrix.ndim)
print("Shape:", matrix.shape)
print("Size:", matrix.size)
print("Data Type:", matrix.dtype)

print("\nArray Operations:")
print("Element at row 2, column 3:", matrix[1][2])
print("First Row:", matrix[0])
print("Second Column:", matrix[:, 1])
print("Transpose:")
print(matrix.T)
print("Row-wise Sum:", np.sum(matrix, axis=1))
print("Column-wise Sum:", np.sum(matrix, axis=0))
