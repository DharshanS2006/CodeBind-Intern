import numpy as np


numbers = np.array([5, 12, 18, 25, 30, 41, 50])

print("Original Array:")
print(numbers)

print("\nBoolean Conditions:")
print("Numbers greater than 20:", numbers > 20)
print("Numbers less than or equal to 30:", numbers <= 30)
print("Even number condition:", numbers % 2 == 0)

print("\nFiltered Arrays:")
print("Numbers greater than 20:", numbers[numbers > 20])
print("Numbers less than or equal to 30:", numbers[numbers <= 30])
print("Even numbers:", numbers[numbers % 2 == 0])
print("Numbers between 10 and 40:", numbers[(numbers >= 10) & (numbers <= 40)])
print("Numbers less than 10 or greater than 40:", numbers[(numbers < 10) | (numbers > 40)])
