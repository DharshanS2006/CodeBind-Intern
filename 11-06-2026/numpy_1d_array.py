import numpy as np


numbers = np.array([10, 20, 30, 40, 50])

print("1D NumPy Array:")
print(numbers)

print("\nArray Information:")
print("Dimensions:", numbers.ndim)
print("Shape:", numbers.shape)
print("Size:", numbers.size)
print("Data Type:", numbers.dtype)

print("\nArray Operations:")
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Array after adding 5:", numbers + 5)
