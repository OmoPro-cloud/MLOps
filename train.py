'''
train a sentiment model with a SageMaker training job
'''
import argpass
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

def model_fn(model_dir):
  return joblib.load(os.path.join(model_dir, "model.joblib"))

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--train", type=str)
  parser.add_argument("--model-dir", type=str, default="/opt/ml/model")
  args = parser.parse_args()

  df = pd.read_csv(args.train)
  x = df["text"]
  y = df["label"]

  vectorizer = TfidVectorizer()
  x = vectorizer.fit_transform(x)

  model = LogisticRegression()
  model.fit(x, y)

  #save model artifacts
  joblib.dump((vectorizer, model), f"{args.model_dir}/model.joblib")