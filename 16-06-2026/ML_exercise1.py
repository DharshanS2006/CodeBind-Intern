import numpy as np
from scipy import stats

marks = [55, 72, 88, 45, 92, 72, 65, 78, 72, 90]

# Mean = average value
mean = np.mean(marks)
print("Mean:", mean)

# Median = middle value when sorted
median = np.median(marks)
print("Median:", median)

# Mode = most frequent value
mode = stats.mode(marks, keepdims=True)
print("Mode:", mode.mode[0])

