from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
import os
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
#from airflow.utils.dates import days_ago
from airflow.exceptions import AirflowFailException

# -------- CONFIGURATION --------
MODEL_THRESHOLD = 0.5  # threshold below which we treat the model as bad

# -------- FUNCTIONS --------
def generate_data(**context):
    """Generate synthetic sales data and save to /tmp/sales_data_{date}.csv."""
    execution_date = context["ds"]  # YYYY-MM-DD
    path = f"/tmp/sales_data_{execution_date}.csv"

    # Generate random data
    np.random.seed(42)
    X = np.random.rand(100, 1) * 10
    y = 2.5 * X.squeeze() + np.random.randn(100) * 2

    df = pd.DataFrame({"feature": X.squeeze(), "sales": y})
    df.to_csv(path, index=False)

    # Push path to XCom
    context["ti"].xcom_push(key="csv_path", value=path)
    return path


def train_model(**context):
    """Read CSV, train LinearRegression model, save to /tmp/model_{date}.pkl."""
    execution_date = context["ds"]
    ti = context["ti"]

    csv_path = ti.xcom_pull(key="csv_path", task_ids="generate_data")
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    df = pd.read_csv(csv_path)
    X = df[["feature"]]
    y = df["sales"]

    model = LinearRegression()
    model.fit(X, y)

    model_path = f"/tmp/model_{execution_date}.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    # Push model path & coefficient to XCom
    ti.xcom_push(key="model_path", value=model_path)
    ti.xcom_push(key="coef", value=float(model.coef_[0]))

    return model_path


def check_model(**context):
    """Fail task if model coefficient is below MODEL_THRESHOLD."""
    ti = context["ti"]
    coef = ti.xcom_pull(key="coef", task_ids="train_model")

    if coef < MODEL_THRESHOLD:
        raise ValueError(
            f"Model coefficient {coef:.4f} is below threshold {MODEL_THRESHOLD:.4f}"
        )
    return f"OK — coef {coef:.4f}"


# -------- DAG DEFINITION --------
with DAG(
    dag_id="sales_retraining",
    schedule="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    default_args={
        "retries": 1,
        "retry_delay": timedelta(minutes=1),
    },
) as dag:
    
    @task
    def extract():
        df = pd.read_csv