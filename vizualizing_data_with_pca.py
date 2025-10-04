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