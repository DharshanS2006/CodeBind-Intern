# Population Variance

data = [10, 20, 30, 40, 50]
n = len(data)
mean = sum(data) / n
population_variance = sum((x - mean) ** 2 for x in data) / n
print("Mean =", mean)
print("Population Variance =", population_variance)
print("-" * 30 )

# Sample Variance

data = [10, 20, 30, 40, 50]
n = len(data)
mean = sum(data) / n
sample_variance = sum((x - mean) ** 2 for x in data) / (n - 1)
print("Mean =", mean)
print("Sample Variance =", sample_variance)
print("-" * 30 )

# Degree of Freedom

data = [10, 20, 30, 40, 50]
n = len(data)
degree_of_freedom = n - 1
print("Number of observations =", n)
print("Degree of Freedom =", degree_of_freedom)
print("-" * 30 )    