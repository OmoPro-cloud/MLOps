import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

def train():
  #Fake data
  x = np.array([[1], [2], [3], [4], [5]])
  y = np.array([2, 4, 6, 8, 10])

  with mlflow.start_run():
    model = LinearRegression()
    model.fit(x, y)
    predictions = model.predict(x)
    mse = mean_squared_error(y, predictions)
    mlflow.log_param("model_type", "LinearRegression")
    mlflow.log_metric("mse", mse)
    mlflow.sklearn.log_model(model, "model")
    print(f"Training complete. MSE {mse}")


if __name__ == "__main__":
  train()