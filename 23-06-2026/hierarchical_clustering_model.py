# Simple Hierarchical Clustering Model

from sklearn.cluster import AgglomerativeClustering

# x = customer data [age, spending score]
x = [
    [20, 25],
    [22, 30],
    [25, 35],
    [45, 70],
    [48, 75],
    [50, 80],
]

# Create hierarchical clustering model with 2 clusters
model = AgglomerativeClustering(n_clusters=2)

# Train the model and get cluster labels
cluster_labels = model.fit_predict(x)

print("Hierarchical Clustering Model")
print("-" * 40)
print("Customer Data =", x)
print("Cluster Labels =", cluster_labels)
print()

for i in range(len(x)):
    print("Customer", i + 1, "belongs to Cluster", cluster_labels[i])
