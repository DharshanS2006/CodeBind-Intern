import numpy as np


cube = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print("3D NumPy Array:")
print(cube)

print("\nArray Information:")
print("Dimensions:", cube.ndim)
print("Shape:", cube.shape)
print("Size:", cube.size)
print("Data Type:", cube.dtype)

print("\nArray Operations:")
print("First 2D Array:")
print(cube[0])
print("Second 2D Array:")
print(cube[1])
print("Element at block 2, row 1, column 3:", cube[1][0][2])
print("Maximum Value:", np.max(cube))
print("Minimum Value:", np.min(cube))
print("Array after multiplying by 2:")
print(cube * 2)
