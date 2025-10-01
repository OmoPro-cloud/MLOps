from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

# Generate synthetic data
X, _ = make_blobs(n_samples=400, centers=3, random_state=42)

#K-Means Implementation

# Model 1
kmeans_optimal = KMeans(n_clusters=3, random_state=0)
labels_optimal = kmeans_optimal.fit_predict(X)
centroids_optimal = kmeans_optimal.cluster_centers_

