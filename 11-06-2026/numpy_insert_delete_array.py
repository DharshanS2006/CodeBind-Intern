import numpy as np


numbers = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(numbers)

after_insert = np.insert(numbers, 2, 25)
print("\nArray after inserting 25 at index 2:")
print(after_insert)

after_append = np.append(numbers, 60)
print("\nArray after appending 60:")
print(after_append)

after_delete = np.delete(numbers, 3)
print("\nArray after deleting element at index 3:")
print(after_delete)

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nOriginal Matrix:")
print(matrix)

print("\nMatrix after inserting a new row:")
print(np.insert(matrix, 1, [7, 8, 9], axis=0))

print("\nMatrix after deleting second column:")
print(np.delete(matrix, 1, axis=1))
