from sklearn.datasets import fetch_california_housing
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

# 1. Load data
data = fetch_california_housing(as_frame=True)
df = data.frame

# 2. Define features and target
X = df.drop(columns=['MedHouseVal'])
y = df['MedHouseVal']

# 3. Split into train and test sets
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Preprocessing pipeline for numeric features
num_features = X.columns.tolist()
num_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    # optionally, you could scale features (e.g. StandardScaler) here
])

preprocessor = ColumnTransformer([
    ('num', num_transformer, num_features)
])

# 5a. Pipeline with Linear Regression model
pipe_lin = Pipeline([
    ('pre', preprocessor),
    ('model', LinearRegression())
])

# 5b. Pipeline with Decision Tree regressor (for comparison)
tree_reg = DecisionTreeRegressor(max_depth=5, random_state=42)
pipe_tree = Pipeline([
    ('pre', preprocessor),
    ('model', tree_reg)
])

# 6. Train on the training data
pipe_lin.fit(x_train, y_train)
pipe_tree.fit(x_train, y_train)

# 7. Predict on test set
y_pred_lin = pipe_lin.predict(x_test)
y_pred_tree = pipe_tree.predict(x_test)

# 8. Evaluate performance for Linear Regression
mse_lin = mean_squared_error(y_test, y_pred_lin)
rmse_lin = np.sqrt(mse_lin)
mae_lin = mean_absolute_error(y_test, y_pred_lin)
r2_lin = r2_score(y_test, y_pred_lin)

print("=== Linear Regression Performance ===")
print(f"RMSE: {rmse_lin:.3f}")
print(f"MAE: {mae_lin:.3f}")
print(f"R² Score: {r2_lin:.3f}")

# 9. Evaluate performance for Decision Tree
mse_tree = mean_squared_error(y_test, y_pred_tree)
rmse_tree = np.sqrt(mse_tree)
mae_tree = mean_absolute_error(y_test, y_pred_tree)
r2_tree = r2_score(y_test, y_pred_tree)

print("\n=== Decision Tree Performance (max_depth=5) ===")
print(f"RMSE: {rmse_tree:.3f}")
print(f"MAE: {mae_tree:.3f}")
print(f"R² Score: {r2_tree:.3f}")

# 10. Visualize the tree (first few levels)
plt.figure(figsize=(20, 8))
plot_tree(
    pipe_tree.named_steps['model'],
    feature_names=num_features,
    filled=True,
    max_depth=3,
    fontsize=10
)
plt.title("Decision Tree (Top 3 Levels) for Predicting MedHouseVal")
plt.show()