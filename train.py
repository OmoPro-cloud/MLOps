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

def train():
    # Use a local tracking URI that is safe in CI (inside the repo)
    mlruns_path = os.path.join(os.getcwd(), "mlruns")
    mlflow.set_tracking_uri(f"file://{mlruns_path}")

    # Optionally, set an experiment name so runs go under a consistent experiment
    #mlflow.set_experiment("ci-experiment")

    with mlflow.start_run():
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

        run = mlflow.active_run()
        artifact_uri = run.info.artifact_uri
        print("Artifact URI:", artifact_uri)

        # Copy the logged model from the mlruns folder to a top-level `models/` dir
        # so GitHub Actions can upload it
        src_model_path = os.path.join(
            mlruns_path,
            run.info.run_id,
            "artifacts",
            "model"
        )
        dst_model_path = os.path.join(os.getcwd(), "models", run.info.run_id)
        os.makedirs(dst_model_path, exist_ok=True)

        # Copy the model folder
        import shutil
        shutil.copytree(src_model_path, os.path.join(dst_model_path, "model"), dirs_exist_ok=True)

        print(f"Copied model to {dst_model_path}")

if __name__ == "__main__":
    train()