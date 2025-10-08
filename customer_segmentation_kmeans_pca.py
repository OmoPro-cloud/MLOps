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