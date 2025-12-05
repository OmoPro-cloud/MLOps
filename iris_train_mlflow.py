'''
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os
import pprint

# Ensure local mlruns directory
mlflow.set_tracking_uri("file:./mlruns")
print("MLflow tracking URI:", mlflow.get_tracking_uri())

def train_and_log():
    data = load_iris()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #model = DecisionTreeClassifier()

    # Start a run and log
    with mlflow.start_run():

    # Train model
      model = DecisionTreeClassifier()
      model.fit(X_train, y_train)
      predictions = model.predict(X_test)

    # accuracy
      accuracy = accuracy_score(y_test, predictions)
    # Log metrics
      mlflow.log_metric("accuracy", accuracy)

    # ✅ Log as MLflow model (this creates the 'model/' folder)
      mlflow.sklearn.log_model(model, artifact_path="model")

if __name__ == "__main__":
    train_and_log()

#mlflow models serve -m "runs:/eef21e7d48474579b3108cf85667bd87/artifacts/artifact_files" -p 5001

'''

import mlflow
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

mlflow.set_tracking_uri("file:./mlruns")

data = load_iris()
x = data.data
y = data.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

models = {
  "DecisionTree": DecisionTreeClassifier()
}

for model_name, model in models.items():
  with mlflow.start_run(run_name=model_name):
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)

    mlflow.log_param("model_type", model_name)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "model")

    print(f"{model_name} has succefully completed training with an accuracy of:\n{accuracy}%")