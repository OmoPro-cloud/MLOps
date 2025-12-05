from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="The wine train classifier is running!")

model = joblib.load('wine_model.pkl')

class WineRequest(BaseModel):
  alcohol_level: float
  malic_acid: float
  flavor: float

@app.get("/")
def home():
  return {"The wine train classifier is running!"}

@app.post("/predict")
def predict_wine(data: WineRequest):
  class_names = {0}
  features = np.array([[data.alcohol_level, data.malic_acid, data.flavor, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
  prediction = model.predict(features)[0]
  return {"prediction": int(prediction)}