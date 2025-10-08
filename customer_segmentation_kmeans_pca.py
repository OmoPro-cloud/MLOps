import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from mpl_toolkits.mplot3d import Axes3D #this is what helps us with 3D plotting

df = pd.read_csv("customers.csv")

print("First 5 rows:")
print(df.head())
print("\nSummary statistics:")
print(df.describe())
print("\nInfo and missing values:")
print(df.info())
print("\nMissing counts per column:")
print(df.isnull().sum())

plt.figure(figsize=(5, 4))
sns.scatterplot(data=df, x="Age", y="Annual Income (k$)")
plt.title("Age vs Annual Income")
plt.show()

plt.figure(figsize=(5, 4))
sns.scatterplot(data=df, x="Annual Income (k$)", y="Spending Score (1-100)")
plt.title("Annual Income vs Spending Score")
plt.show()

plt.figure(figsize=(5, 4))
sns.scatterplot(data=df, x="Age", y="Spending Score (1-100)")
plt.title("Age vs Spending Score")
plt.show()

# 3. K‑Means Clustering

# Select features
features = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
X = df[features].values

# finding k with the elbow method
inertias = []
K_range = range(1, 11)
for k in K_range:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X)
    inertias.append(km.inertia_)

plt.figure(figsize=(6, 4))
plt.plot(K_range, inertias, marker='o')
plt.xlabel("Number of clusters k")
plt.ylabel("Inertia")
plt.title("Elbow Method to Determine Optimal k")
plt.xticks(K_range)
plt.show()

optimal_k = 5
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
labels = kmeans.fit_predict(X)
df["Cluster"] = labels

# 3D scatter plot of clusters
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(
    df["Age"], df["Annual Income (k$)"], df["Spending Score (1-100)"],
    c=df["Cluster"], cmap="tab10", s=50, alpha=0.7
)
ax.set_xlabel("Age")
ax.set_ylabel("Annual Income (k$)")
ax.set_zlabel("Spending Score (1-100)")
plt.title("Clusters in 3D (Age, Income, Spending Score)")

legend1 = ax.legend(*scatter.legend_elements(), title="Cluster")
ax.add_artist(legend1)
plt.show()

#PCA (Principle COmponent Analysis/Dimensionality Reduction)

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


pca = PCA(n_components=2, random_state=42)# PCA to 2 components
X_pca = pca.fit_transform(X_scaled)

# Append PCA results to df
df["PCA1"] = X_pca[:, 0]
df["PCA2"] = X_pca[:, 1]

# Plot clusters in PCA space
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x="PCA1", y="PCA2", hue="Cluster", palette="tab10", s=60, alpha=0.8)
plt.title("Cluster visualization in PCA‑reduced space")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.legend(title="Cluster")
plt.show()

# 5. Interpret Results

cluster_summary = df.groupby("Cluster")[features].mean().reset_index()
print("Cluster centroids (mean values):")
print(cluster_summary)

# Optional: also display cluster sizes
cluster_counts = df["Cluster"].value_counts().sort_index()
print("\nCluster sizes:")
print(cluster_counts)

# Write interpretation (you’ll put this in markdown in your notebook)
for idx, row in cluster_summary.iterrows():
    print(f"Cluster {int(row['Cluster'])}: Age ≈ {row['Age']:.1f}, Income ≈ {row['Annual Income (k$)']:.1f}, "
          f"Spending Score ≈ {row['Spending Score (1-100)']:.1f}")

# (You’d then write 5–6 lines summarizing what these clusters look like: e.g.
# Cluster 0 — young, moderate income, high spenders; Cluster 1 — older, high income but low spenders, etc.)

# Bonus: pairplot with clusters
sns.pairplot(df, vars=features, hue="Cluster", palette="tab10", diag_kind="kde", height=2.5)
plt.suptitle(" Bonus Pairplot of features colored by cluster", y=1.02)
plt.show()