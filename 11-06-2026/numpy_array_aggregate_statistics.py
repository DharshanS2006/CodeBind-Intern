import numpy as np


marks = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [95, 91, 89]
])

print("Marks Array:")
print(marks)

print("\nOverall Statistics:")
print("Sum:", np.sum(marks))
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))
print("Standard Deviation:", np.std(marks))

print("\nSubject-wise Statistics:")
print("Column-wise Sum:", np.sum(marks, axis=0))
print("Column-wise Average:", np.mean(marks, axis=0))

print("\nStudent-wise Statistics:")
print("Row-wise Sum:", np.sum(marks, axis=1))
print("Row-wise Average:", np.mean(marks, axis=1))
