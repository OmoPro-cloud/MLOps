'''
pca's main use is vizualisation
data is reduced from multidimensional to 2d and 3d, this makes it easier to plot
pca reduces noise by removing the 
pca will find a new axis
antagonal components
pca is the process of automatically finding the best angle
pca is essential for reducing data to 2 and 3 dimensional
pca can be used to speed up model by reducing the feature count(makes linear regression faster)
pca is useful in vizualition
in python we still use sci-kit learn on PCA'''

from sklearn.decomposition import PCA
from sklearn.datasets import load_digits

digits = load_digits()
X =digits.data

#Each image is 8x8 pixels, so X has 64 dimensions(features)
print(f"Original shape: {X.shape}")

#Instantiate PCA to reduce to 2 dimensions
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print(f"Reduced Shape: {X_reduced.shape}")

#KMeans is for clustering while PCA is for dimensionality reduction
#we can reduce multidimensional data into 2 dimensional or 3 dimensional data