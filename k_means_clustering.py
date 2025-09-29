import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

#Generate Synthetic Data
x, y = make_blobs(n_samples=300, centers=4, random_state=42)

#Fit KMeans model
kmeans = KMeans(n_clusters=4, random_state=42)
y_predict = kmeans.fit_predict(x)

#Plot the clusters
plt.scatter(x[:, 0], x[:, 1], c=y_predict, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='x')
plt.title('K-Means Clustering Example')
plt.show()