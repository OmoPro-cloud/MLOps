import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier

mlflow.set_tracking_uri("file:./mlruns")

data = load_wine()
x = data.data
y = data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

models = {
  "DecisionTree": DecisionTreeClassifier(),
  #"LinearRegression": LinearRegression(),
  #"RandomForest": RandomForestClassifier()
}

for model_name, model in models.items():
  with mlflow.start_run(run_name=model_name):
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)
  
    mlflow.log_param("model_type", model_name)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "model")

    print(f"{model_name} trained with accuracy: {accuracy}")
# mlflow models serve -m "./mlruns/0/models/m-30023a3d4bb245279fc253d08a8dde08/" -p 5001