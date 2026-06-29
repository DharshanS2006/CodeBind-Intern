# Simple DBSCAN Clustering Model

from sklearn.cluster import DBSCAN

# x = customer data [age, spending score]
x = [
    [20, 25],
    [21, 26],
    [22, 28],
    [45, 70],
    [46, 72],
    [47, 74],
    [80, 10],
]

# Create DBSCAN model
# eps = maximum distance between nearby points
# min_samples = minimum points needed to form a cluster
model = DBSCAN(eps=5, min_samples=2)

# Train the model and get cluster labels
cluster_labels = model.fit_predict(x)

print("DBSCAN Clustering Model")
print("-" * 35)
print("Customer Data =", x)
print("Cluster Labels =", cluster_labels)
print()
print("Note: Label -1 means noise or outlier")
print()

for i in range(len(x)):
    print("Customer", i + 1, "belongs to Cluster", cluster_labels[i])
