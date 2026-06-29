import numpy as np


numbers = np.array([45, 12, 89, 33, 27, 68, 10, 92])

print("Original Array:")
print(numbers)

print("\nBasic Information:")
print("Dimensions:", numbers.ndim)
print("Shape:", numbers.shape)
print("Size:", numbers.size)
print("Data Type:", numbers.dtype)

print("\nIndexing and Slicing:")
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])
print("First Four Elements:", numbers[:4])
print("Reverse Array:", numbers[::-1])

print("\nArithmetic Operations:")
print("Add 10:", numbers + 10)
print("Subtract 5:", numbers - 5)
print("Multiply by 2:", numbers * 2)
print("Divide by 2:", numbers / 2)

print("\nSorting and Filtering:")
print("Sorted Array:", np.sort(numbers))
print("Descending Order:", np.sort(numbers)[::-1])
print("Even Numbers:", numbers[numbers % 2 == 0])
print("Odd Numbers:", numbers[numbers % 2 != 0])
print("Numbers greater than 40:", numbers[numbers > 40])

print("\nStatistical Operations:")
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Median:", np.median(numbers))
print("Minimum:", np.min(numbers))
print("Maximum:", np.max(numbers))
print("Standard Deviation:", np.std(numbers))

print("\nInsert, Append, and Delete:")
print("Insert 100 at index 2:", np.insert(numbers, 2, 100))
print("Append 200:", np.append(numbers, 200))
print("Delete element at index 3:", np.delete(numbers, 3))

print("\nSearch Operations:")
print("Position of 68:", np.where(numbers == 68)[0])
print("Positions of even numbers:", np.where(numbers % 2 == 0)[0])

print("\nReshape and Flatten:")
matrix = numbers.reshape(2, 4)
print("Reshaped Matrix:")
print(matrix)
print("Flattened Array:", matrix.flatten())

print("\nCumulative Operations:")
print("Cumulative Sum:", np.cumsum(numbers))
print("Cumulative Product:", np.cumprod(numbers))
