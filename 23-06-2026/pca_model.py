# Simple PCA Model

from sklearn.decomposition import PCA

# x = student data [math marks, science marks, english marks]
x = [
    [80, 85, 78],
    [82, 88, 80],
    [85, 90, 82],
    [40, 45, 50],
    [42, 48, 52],
    [45, 50, 55],
]

# Create PCA model to reduce 3 features into 2 features
model = PCA(n_components=2)

# Train the model and transform the data
new_data = model.fit_transform(x)

print("PCA Model")
print("-" * 25)
print("Original Student Data =", x)
print()
print("Data After PCA:")
print(new_data)
print()
print("Explained Variance Ratio =", model.explained_variance_ratio_)
