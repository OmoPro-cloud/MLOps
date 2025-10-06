from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

#load data
data = fetch_california_housing(as_frame=True)
df = data.frame

#create feature and target
X = df.drop(columns=['MedHouseVal'])
y = df['MedHouseVal']

#train test split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing pipeline
num_features = X.columns.tolist()
num_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])
preprocessor = ColumnTransformer([
    ('num', num_transformer, num_features)
])

# here I fit the preprocessor on the *training* data, and transform both train & test
X_train_scaled = preprocessor.fit_transform(x_train)
X_test_scaled = preprocessor.transform(x_test)

# (Optional) If you want to run the regression as well
pipe = Pipeline([
    ('pre', preprocessor),
    ('model', LinearRegression())
])
pipe.fit(x_train, y_train)
y_pred = pipe.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"RMSE: {rmse:.3f}, MAE: {mae:.3f}, R2: {r2:.3f}")



#PCA Scale
X_scaled_full = np.vstack([X_train_scaled, X_test_scaled])

pca_full = PCA(n_components=8)
pca_full.fit(X_scaled_full)
explained = pca_full.explained_variance_ratio_

print("Explained variance ratio per component:")
for i, frac in enumerate(explained, start=1):
    print(f"  PC{i}: {frac:.4f} ({frac*100:.2f}%)")

#sum of first two components
sum_first2 = explained[0] + explained[1]
print(f"Sum of first two explained variance ratios: {sum_first2:.4f} ({sum_first2*100:.2f}%)")

# plot of variance between cumulative explained
cum_explained = np.cumsum(explained)
plt.figure(figsize=(8,5))
plt.plot(range(1, 9), cum_explained, marker='o', linestyle='--')
plt.xlabel("Number of principal components")
plt.ylabel("Cumulative explained variance ratio")
plt.title("Cumulative explained variance by # of PCs")
plt.grid(True)
plt.axhline(0.90, color='red', linestyle=':')  # makes a horizontal line at 90%
plt.show()

# Determine how many PCs to reach ≥ 90%
num_needed = np.argmax(cum_explained >= 0.90) + 1  # +1 because zero-based index
print(f"Number of PCs needed to explain ≥90% variance: {num_needed}")

# reduce to 2D and vizualize

pca2 = PCA(n_components=2)
X_reduced_2d = pca2.fit_transform(X_scaled_full)

# For coloring, we need the corresponding y values for full data (train + test)
y_full = np.concatenate([y_train.to_numpy(), y_test.to_numpy()])

# Create HighValue binary indicator
HighValue = (y_full > 3.0).astype(int)

# Plot
plt.figure(figsize=(8,6))
scatter = plt.scatter(
    X_reduced_2d[:, 0], X_reduced_2d[:, 1],
    c=HighValue,
    cmap='coolwarm',  # red/blue coloring
    alpha=0.6,
    s=20
)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("2D PCA projection of California Housing, colored by HighValue")
plt.colorbar(scatter, label="HighValue (0 = low, 1 = high)")
plt.show()