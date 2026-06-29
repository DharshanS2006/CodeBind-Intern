# Simple K-Means Clustering Model

import os

os.environ["LOKY_MAX_CPU_COUNT"] = "4"

from sklearn.cluster import KMeans

# x = customer data [age, spending score]
x = [
    [20, 25],
    [22, 30],
    [25, 35],
    [45, 70],
    [48, 75],
    [50, 80],
]

# Create K-Means model with 2 clusters
model = KMeans(n_clusters=2, random_state=0, n_init=10)

# Train the model
model.fit(x)

print("K-Means Clustering Model")
print("-" * 35)
print("Customer Data =", x)
print("Cluster Labels =", model.labels_)
print("Cluster Centers =", model.cluster_centers_)
print()

# Predict cluster for a new customer
new_customer = [[30, 40]]
predicted_cluster = model.predict(new_customer)

print("New Customer =", new_customer[0])
print("Predicted Cluster =", predicted_cluster[0])
