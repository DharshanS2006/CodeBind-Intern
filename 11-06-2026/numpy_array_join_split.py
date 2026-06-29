import numpy as np


first_array = np.array([1, 2, 3, 4])
second_array = np.array([5, 6, 7, 8])

print("First Array:")
print(first_array)

print("\nSecond Array:")
print(second_array)

joined_array = np.concatenate((first_array, second_array))
print("\nJoined 1D Array:")
print(joined_array)

split_arrays = np.array_split(joined_array, 4)
print("\nSplit 1D Array into 4 parts:")
for index, part in enumerate(split_arrays, start=1):
    print("Part", index, ":", part)

first_matrix = np.array([[1, 2], [3, 4]])
second_matrix = np.array([[5, 6], [7, 8]])

print("\nFirst Matrix:")
print(first_matrix)

print("\nSecond Matrix:")
print(second_matrix)

print("\nJoined by Rows:")
print(np.vstack((first_matrix, second_matrix)))

print("\nJoined by Columns:")
print(np.hstack((first_matrix, second_matrix)))
