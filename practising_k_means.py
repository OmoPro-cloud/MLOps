import matplotlib as plt
from sklearn.datasets import make_blobs #this import allows us to generate blobs for clustering
from sklearn.cluster import KMeans #allows us to create(map?) clusters

'''
Q: what is random_state ?
A: random_state is a parameter that controls the “seed” or internal state of a pseudo‑random number generator. Its main purpose is to make operations that involve randomness reproducible
'''

#Generate synthetic data
x, y = make_blobs(n_samples=300, centers=4, random_state=42)

#Fit KMeans model
kmeans = KMeans(n_clusters=4, random_state=42)
y_predict = kmeans.fit_predict(x)

#Plot the cluster
plt.scatter(x[:, 0], x[:, 1], c=y_predict, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='x')
plt.title('K-Means Clusterinf Example')
plt.show()