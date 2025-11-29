from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Iris Classifier API")

model = joblib.load('iris_model.pkl')

class IrisRequest(BaseModel):
  sepal_length: float
  sepal_width: float
  petal_length: float
  petal_width: float

@app.get("/")
def home():
  return {"message": "Iris model API is running!"}

@app.post("/predict")
def predict_iris(data: IrisRequest):
  class_names = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
  features = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
  prediction = model.predict(features)[0]
  return {"prediction": class_names[int(prediction)]}
  #return {"prediction": int(prediction)}