import numpy as np


numbers = np.array([5, 10, 15, 20, 25, 30, 35, 40])
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("1D Array:")
print(numbers)

print("\nIndexing in 1D Array:")
print("First Element:", numbers[0])
print("Fourth Element:", numbers[3])
print("Last Element:", numbers[-1])

print("\nSlicing in 1D Array:")
print("Elements from index 2 to 5:", numbers[2:6])
print("Every second element:", numbers[::2])
print("Reverse array:", numbers[::-1])

print("\n2D Array:")
print(matrix)

print("\nIndexing and Slicing in 2D Array:")
print("Element at row 2, column 3:", matrix[1, 2])
print("First row:", matrix[0, :])
print("Third column:", matrix[:, 2])
print("First two rows and first three columns:")
print(matrix[:2, :3])
