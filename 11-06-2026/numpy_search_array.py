import numpy as np


numbers = np.array([12, 45, 23, 45, 67, 89, 45, 10])

print("Array:")
print(numbers)

search_value = 45
positions = np.where(numbers == search_value)

print("\nSearch Value:", search_value)
print("Positions:", positions[0])
print("Number of Times Found:", len(positions[0]))

print("\nNumbers greater than 40 are at positions:")
print(np.where(numbers > 40)[0])

print("\nNumbers divisible by 5 are at positions:")
print(np.where(numbers % 5 == 0)[0])
