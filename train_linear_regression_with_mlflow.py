'''import mlflow
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
  train()'''

import os
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import shutil

def train():
    mlruns_path = os.path.join(os.getcwd(), "mlruns")
    mlflow.set_tracking_uri(f"file://{mlruns_path}")
    mlflow.set_experiment("ci-experiment")

    with mlflow.start_run() as run:
        # Fake data
        x = np.array([[1], [2], [3], [4], [5]])
        y = np.array([2, 4, 6, 8, 10])

        model = LinearRegression()
        model.fit(x, y)
        predictions = model.predict(x)
        mse = mean_squared_error(y, predictions)

        mlflow.log_param("model_type", "LinearRegression")
        mlflow.log_metric("mse", mse)
        mlflow.sklearn.log_model(model, "model")

        print(f"Training complete. MSE {mse}")

        run_id = run.info.run_id
        artifact_uri = run.info.artifact_uri
        print("Run ID:", run_id)
        print("Artifact URI:", artifact_uri)

        # Construct the path to the model artifact directory
        # According to MLflow layout: mlruns/{experiment_id}/{run_id}/artifacts/{artifact_path}
        # Since you used artifact_path="model" in log_model, it's under `artifacts/model`
        # But you must also know the experiment id to build the path. You can get it from run.info.experiment_id
        experiment_id = run.info.experiment_id

        src_model_path = os.path.join(
            mlruns_path,
            experiment_id,
            run_id,
            "artifacts",
            "model"
        )

        if not os.path.isdir(src_model_path):
            raise FileNotFoundError(f"Model folder not found at expected path: {src_model_path}")

        dst_model_path = os.path.join(os.getcwd(), "models", run_id)
        os.makedirs(dst_model_path, exist_ok=True)

        shutil.copytree(src_model_path, os.path.join(dst_model_path, "model"))

        print(f"Copied model artifacts to {dst_model_path}")

if __name__ == "__main__":
    train()