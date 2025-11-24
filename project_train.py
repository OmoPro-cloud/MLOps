import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature

from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

if __name__ == "__main__":
    data = fetch_california_housing()
    X = data.data
    y = data.target
    print(f"Loaded California housing: X shape = {X.shape}, y shape = {y.shape}")

    # Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Use only Linear Regression
    model = LinearRegression()
    print("Training Linear Regression on California housing data")

    mlflow.start_run()

    # Log parameters
    mlflow.log_param("dataset", "california_housing")
    mlflow.log_param("n_samples", X.shape[0])
    mlflow.log_param("n_features", X.shape[1])
    mlflow.log_param("test_size", 0.2)
    mlflow.log_param("random_state", 42)

    # Log model hyperparameters
    for name, val in model.get_params().items():
        try:
            mlflow.log_param(name, val)
        except Exception:
            pass

    # Train the model
    model.fit(X_train, y_train)

    # Predict on test
    y_pred = model.predict(X_test)

    # Compute metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Log metrics
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("r2", r2)

    # Log model artifact
    signature = infer_signature(X_train, model.predict(X_train))
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="linear_regression_model",
        signature=signature,
        input_example=X_train[:5]
    )

    # Print metrics
    print(f"MSE on test set: {mse:.4f}")
    print(f"R2 on test set: {r2:.4f}")
    print(f"MLflow run ID: {mlflow.active_run().info.run_id}") #

    mlflow.end_run()