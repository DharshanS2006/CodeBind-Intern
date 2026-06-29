#Population Standard Deviation

import math
data = [10, 20, 30, 40, 50]
n = len(data)
mean = sum(data) / n
population_variance = sum((x - mean) ** 2 for x in data) / n
population_std = math.sqrt(population_variance)
print("Mean =", mean)
print("Population Variance =", population_variance)
print("Population Standard Deviation =", population_std)
print("-" * 30 )    

#Sample Standard Deviation

import math
data = [10, 20, 30, 40, 50]
n = len(data)
mean = sum(data) / n
sample_variance = sum((x - mean) ** 2 for x in data) / (n - 1)
sample_std = math.sqrt(sample_variance)
print("Mean =", mean)
print("Sample Variance =", sample_variance)
print("Sample Standard Deviation =", sample_std)
print("-" * 30 )    