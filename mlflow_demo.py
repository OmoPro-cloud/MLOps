import mlflow
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing()
X, y = data.data, data.target

model = LinearRegression()

with mlflow.start_run():
  model.fit(X, y)
  predictions = model.predict(X)
  mse = mean_squared_error(y, predictions)

  mlflow.log_param("model_type", "LinearRegression")
  mlflow.log_metric("mse", mse)
  mlflow.sklearn.log_model(model, "linear_regression_model")