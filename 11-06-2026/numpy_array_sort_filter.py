import numpy as np


numbers = np.array([45, 12, 89, 33, 27, 68, 10, 92])

print("Original Array:")
print(numbers)

print("\nSorted Array:")
print(np.sort(numbers))

print("\nDescending Order:")
print(np.sort(numbers)[::-1])

print("\nFiltering Operations:")
print("Numbers greater than 40:", numbers[numbers > 40])
print("Even numbers:", numbers[numbers % 2 == 0])
print("Numbers between 20 and 70:", numbers[(numbers >= 20) & (numbers <= 70)])

matrix = np.array([
    [9, 3, 7],
    [4, 8, 2],
    [6, 1, 5]
])

print("\nOriginal Matrix:")
print(matrix)

print("\nSort each row:")
print(np.sort(matrix, axis=1))

print("\nSort each column:")
print(np.sort(matrix, axis=0))
