from datetime import timedelta
import os
import json
from airflow import DAG
from airflow.decorators import task
from airflow.utils.dates import days_ago
from airflow.utils.email import send_email #optional
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#config
DATA_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
BASE_URL = "/tmp/airflow_ml"
RAW_PATH = os.path.join(BASE_URL, "raw.csv")
PROCESSED_PATH = os.path.join(BASE_URL, "processed.csv")
MODEL_PATH = os.path.join(BASE_URL, "model.joblib")

default_args = {
  'owner': 'airflow_yemi',
  'depends_on_past': False,
  'email_on_failure': False,
  'email_on_retry': False,
  'retries': 1,
  'retry_delay': timedelta(minutes=5)
}

with DAG(
  dag_id='etl_train_eval_dag',
  default_args=default_args,
  description='An ETL, Train, and Evaluate DAG for Iris dataset',
  schedule_interval="@daily",
  start_date=days_ago(1),
  catchup=False,
  max_active_runs=1,
  tags=['ml', 'etl', 'iris'],
) as dag:
  
  @task
  def extract():
    df = pd.read_csv(DATA_URL)
    os.makedirs(BASE_URL, exist_ok=True)
    df.to_csv(RAW_PATH, index=False)
    return RAW_PATH
  
  @task
  def transform(raw_path: str):
    df = pd.read_csv(raw_path)
    #a simple transformation: drop N/A and rename column if necessary
    df = df.dropna()
    df.to_csv(PROCESSED_PATH, index=False)
    return PROCESSED_PATH
  
  @task
  def train(processed_path: str):
    df = pd.read_csv(processed_path)
    X = df.drop(columns=["species"])
    y = df["species"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump({"model": model, "columns": list(X.columns)}, MODEL_PATH)
    return MODEL_PATH

  @task
  def evaluate(train_output: str):
    payload = json.loads(train_output)
    model_art = joblib.load(payload["model_path"])
    model = model_art["model"]
    test_df = pd.read_csv(payload["test_path"])
    X_test = test_df[model_art["columns"]]
    y_test = test_df["species"]
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    #push metric to Xcom(return value get stored)
    return {"accuracy": float(acc)}
    
  @task
  def register(metrics: dict):
    #simple "register": write metrics to a file or optionally push to S3 MLFlow
    os.makedirs(BASE_URL, exist_ok=True)
    metrics_path = os.path.join(BASE_URL, "metrics.json")
    with open(metrics_path, "w") as f:
      json.dump(metrics, f)
    return metrics_path
    
  #pipeline wiring
  raw = extract()
  processed = transform(raw)
  train_out = train(processed)
  metrics = evaluate(train_out)
  reg = register_metrics