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