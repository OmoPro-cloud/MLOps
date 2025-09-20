from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import r2_score
from sklearn.compose import ColumnTransformer
from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.discriminant_analysis import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

#load data
data = fetch_california_housing(as_frame=True)
df = data.frame
#print(df.head())

#Features and target
X = df.drop(columns=['MedHouseVal'])
y = df['MedHouseVal']

#Train-test split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Pre-processing (numeric only here)
num_features = X.columns.tolist()
num_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    #('scaler', StandardScaler())
])

preprocessor = ColumnTransformer([
    ('num', num_transformer, num_features)
])

#Full pipeline: preprocessing -> Linear Regression
pipe = Pipeline([
    ('pre', preprocessor),
    ('model', LinearRegression())
])
pipe.fit(x_train, y_train)
y_pred = pipe.predict(x_test)

#Metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"RMSE: {rmse:.3f}, MAE: {mae:.3f}, R2: {r2:.3f}")

# Baseline: always predict mean of training y
baseline_pred = np.full(shape=y_test.shape, fill_value=np.mean(y_train))
baseline_mse = mean_squared_error(y_test, baseline_pred)
baseline_rmse = np.sqrt(baseline_mse)
print(f"Baseline RMSE: {baseline_rmse:.3f}")

'''
RMSE:
MAE: Mean Absolute Error - shows that our predictions could be off by 53.3%
R2: Route Squared - 
Standard Scaler will standardize everything, it will put all features on a similar scale(yen, naira, euros converted to dollars) before comparing them
'''