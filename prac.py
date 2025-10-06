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
x_train, x_split, y_train, y_split = train_test_split(X, y, train_size=0.2, random_state=42)

#Preprocessing Pipeline
num_features = X.columns.tolist()
num_transformer = Pipeline([
  ('imputer', SimpleImputer(strategy='median')),
  ('scaler', StandardScaler())
])
preprocessor = ColumnTransformer([
  ('num', num_transformer, num_features)
])