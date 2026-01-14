from kfp.dsl import component

@component(base_image="python:3.12")
def load_data() -> str:
  import pandas as pd
  df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
  path = "/tmp/iris.csv"
  df.to_csv(path, index=False)
  return path

#Train the model
@component(base_image="python:3.12")
def train_model(data_path: str) -> str:
  import pandas as pd
  from sklearn.linear_model import LogisticRegression
  import joblib

  df = pd.read_csv(data_path)
  X = df.drop("species", axis=1)
  y = df["species"]

  model = LogisticRegression(max_iter=200)
  model.fit(X, y)
  model_path = "/tmp/model.joblib"
  joblib.dump(model, model_path)
  return model_path

@component(base_image="python:3.12")
def evaluate_model(model_path: str, data_path: str) -> float:
  import pandas as pd
  import joblib
  from sklearn.metrics import accuracy_score

  df = pd.read_csv(data_path)
  X = df.drop("species", axis=1)
  y = df["species"]

  model = joblib.load(model_path)
  predictions = model.predict(X)
  accuracy = accuracy_score(y, predictions)
  return accuracy

#define the pipeline
from kfp.dsl import pipeline
@pipeline(name="Iris Classification Pipeline", description="A simple pipeline that trains and evaluates a model on the iris dataset.")
def training_pipeline():
  data_path = load_data()
  model_path = train_model(data_path=data_path.output)
  accuracy = evaluate_model(model_path=model_path.output, data_path=data_path.output)

#compile a pipeline to YAML
from kfp import compiler
compiler.Compiler().compile(pipeline_func=training_pipeline, package_path="iris_pipeline.yaml")

#to run the pipeline, use the kfp sdk or ui to execute the generated yaml files
import kfp
client = kfp.Client()
experiment = client.create_run_from_pipeline_package(
  pipeline_file='iris_pipeline.yaml',
  arguments={}
)