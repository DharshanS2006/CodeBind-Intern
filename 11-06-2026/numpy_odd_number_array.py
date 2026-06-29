import numpy as np


numbers = np.arange(1, 21)

print("Original Array:")
print(numbers)

odd_numbers = numbers[numbers % 2 != 0]

print("\nOdd Numbers:")
print(odd_numbers)

print("\nOdd Numbers after Adding 5:")
print(odd_numbers + 5)

print("\nSum of Odd Numbers:", np.sum(odd_numbers))
print("Mean of Odd Numbers:", np.mean(odd_numbers))
print("Maximum Odd Number:", np.max(odd_numbers))
print("Minimum Odd Number:", np.min(odd_numbers))
