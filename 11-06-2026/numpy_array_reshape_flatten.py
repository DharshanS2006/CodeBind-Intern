import numpy as np


numbers = np.arange(1, 13)

print("Original Array:")
print(numbers)
print("Shape:", numbers.shape)

reshaped_matrix = numbers.reshape(3, 4)
print("\nReshaped into 3 rows and 4 columns:")
print(reshaped_matrix)
print("Shape:", reshaped_matrix.shape)

reshaped_cube = numbers.reshape(2, 2, 3)
print("\nReshaped into 3D Array:")
print(reshaped_cube)
print("Shape:", reshaped_cube.shape)

flattened_array = reshaped_matrix.flatten()
print("\nFlattened Array:")
print(flattened_array)

raveled_array = reshaped_cube.ravel()
print("\nRaveled Array:")
print(raveled_array)
