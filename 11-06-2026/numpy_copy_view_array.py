import numpy as np


numbers = np.array([10, 20, 30, 40, 50])

array_copy = numbers.copy()
array_view = numbers.view()

print("Original Array:")
print(numbers)

array_copy[0] = 100
print("\nAfter changing copy:")
print("Original Array:", numbers)
print("Copy:", array_copy)

array_view[1] = 200
print("\nAfter changing view:")
print("Original Array:", numbers)
print("View:", array_view)

print("\nCopy owns data:", array_copy.base is None)
print("View owns data:", array_view.base is None)
