from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

#Generate synthetic data
X, _ = make_blobs(n_samples=400, centers=3, random_state=42)

# K-Means Implementation

#Model 1
kmeans_optimal = KMeans(n_clusters=3, random_state=0) #shows what optimal clustering looks like
labels_optimal = kmeans_optimal.fit_predict(X)
centroids_optimal = kmeans_optimal.cluster_centers_

#Model 2
kmeans_suboptimal = KMeans(n_clusters=5, random_state=0) #this gives us an example of suboptimal clustering
labels_suboptimal = kmeans_suboptimal.fit_predict(X)
centroids_suboptimal = kmeans_suboptimal.cluster_centers_

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

#Plotting graphs
#plot 1
axes[0].scatter(X[:, 0], X[:, 1], c=labels_optimal, cmap='viridis', s=30)
axes[0].scatter(centroids_optimal[:, 0], centroids_optimal[:, 1], 
                marker='o', s=100, c='red', label='Center')
axes[0].set_title("Optimal Clustering: k=3")
axes[0].legend()

#plot 2
axes[1].scatter(X[:, 0], X[:, 1], c=labels_suboptimal, cmap='viridis', s=30)
axes[1].scatter(centroids_suboptimal[:, 0], centroids_suboptimal[:, 1], 
                marker='o', s=100, c='red', label='Center')
axes[1].set_title("Suboptimal Clustering: k=5")
axes[1].legend()

plt.tight_layout()
plt.show()