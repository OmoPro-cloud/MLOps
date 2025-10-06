'''PCA(principle Component Analysis)'''

from sklearn.decomposition import PCA
from sklearn.datasets import load_digits

print("This mini-project shows how to manipulate multidimensional data and transform it into 2 dimensional data")
print(f"We do this to make data easier to plot on a graph")

digits = load_digits()
X = digits.data

print(f"Original Shape: {X.shape}")

pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print(f"Reduced Shape: {X_reduced.shape}")




'''CUSTOMER SEGMENTATION PROJECT USING KMEANS'''


