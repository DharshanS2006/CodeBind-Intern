import numpy as np


numbers = np.array([10, 20, 10, 30, 20, 40, 50, 30, 10])

print("Original Array:")
print(numbers)

unique_values = np.unique(numbers)
print("\nUnique Values:")
print(unique_values)

unique_values, counts = np.unique(numbers, return_counts=True)

print("\nValue Counts:")
for value, count in zip(unique_values, counts):
    print(value, "appears", count, "time(s)")

print("\nTotal Unique Values:", len(unique_values))
