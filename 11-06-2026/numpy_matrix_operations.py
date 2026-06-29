import numpy as np


first_matrix = np.array([
    [1, 2],
    [3, 4]
])

second_matrix = np.array([
    [5, 6],
    [7, 8]
])

print("First Matrix:")
print(first_matrix)

print("\nSecond Matrix:")
print(second_matrix)

print("\nMatrix Addition:")
print(first_matrix + second_matrix)

print("\nMatrix Subtraction:")
print(first_matrix - second_matrix)

print("\nElement-wise Multiplication:")
print(first_matrix * second_matrix)

print("\nMatrix Multiplication:")
print(np.dot(first_matrix, second_matrix))

print("\nTranspose of First Matrix:")
print(first_matrix.T)

print("\nDeterminant of First Matrix:")
print(np.linalg.det(first_matrix))

print("\nInverse of First Matrix:")
print(np.linalg.inv(first_matrix))
