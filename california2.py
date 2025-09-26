from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.dummy import DummyClassifier
import numpy as np
from sklearn.metrics import classification_report, r2_score, roc_auc_score
from sklearn.compose import ColumnTransformer
from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.discriminant_analysis import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeRegressor, plot_tree
from matplotlib import pyplot as plt

#load data
data = fetch_california_housing(as_frame=True)
df = data.frame
#print(df.head())

#Features and target
X = df.drop(columns=['MedHouseVal'])
y = df['MedHouseVal']

#Train-test split(train linear regression)
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

# Baseline
baseline_pred = np.full(shape=y_test.shape, fill_value=np.mean(y_train))
baseline_mse = mean_squared_error(y_test, baseline_pred)
baseline_rmse = np.sqrt(baseline_mse)
print(f"Baseline RMSE: {baseline_rmse:.3f}")

'''
RMSE: Root Means Squared Error
MAE: Mean Absolute Error - shows that our predictions could be off by 53.3%
R2: Route Squared - this metric is used to judge how well a regression model fits the data
Standard Scaler will standardize everything, it will put all features on a similar scale(yen, naira, euros converted to dollars) before comparing them
'''

#binary target
df = data.frame.copy()
df['High_Price'] = (df['MedHouseVal'] > df['MedHouseVal'].median()).astype(int)
X = df.drop(columns=['MedHouseVal', 'High_Price'])
y = df['High_Price']

x_tr, x_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
#print(df.head())

#Train logistics regression
pipe_clf = Pipeline([
  ('pre', preprocessor),
  ('model', LogisticRegression())
])
pipe_clf.fit(x_tr, y_tr)
y_hat = pipe_clf.predict(x_te)

#Metrics
#print(classification_report(y_te, y_hat))
#print("ROC AUC:", roc_auc_score(y_te, pipe_clf.predict_proba(x_te)[:, 1]))

# Dummy Classifier baseline
#dummy_clf = Pipeline([
#    ('pre', preprocessor),  
#    ('model', DummyClassifier(strategy="most_frequent"))
#])
#dummy_clf.fit(x_tr, y_tr)
#y_dummy = dummy_clf.predict(x_te)
#print("Dummy Classifier results:")
#print(classification_report(y_te, y_dummy))

#linear regression will predict the exact number(e.g. will predict the exact house price)
#logistics regression is for classification. it will calculate the probability of an out(e.g. 75% chance that a house is overpriced)

#Decision Tree
tree = DecisionTreeRegressor(max_depth=5, random_state=42)
pipe_tree = Pipeline([
  ('pre', preprocessor),
  ('model', tree)
])
pipe_tree.fit(x_train, y_train)

#Vizualize the tree
plt.figure(figsize=(20,8))
plot_tree(pipe_tree.named_steps['model'], filled=True, feature_names=num_features, max_depth=3)
plt.show()