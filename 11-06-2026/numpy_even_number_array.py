import numpy as np


numbers = np.arange(1, 21)

print("Original Array:")
print(numbers)

even_numbers = numbers[numbers % 2 == 0]

print("\nEven Numbers:")
print(even_numbers)

print("\nEven Numbers after Multiplying by 2:")
print(even_numbers * 2)

print("\nSum of Even Numbers:", np.sum(even_numbers))
print("Mean of Even Numbers:", np.mean(even_numbers))
print("Maximum Even Number:", np.max(even_numbers))
print("Minimum Even Number:", np.min(even_numbers))
