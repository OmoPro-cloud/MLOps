from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="The wine classifier API is running!")

model = joblib.load('wine_model.pkl')

class WineRequest(BaseModel):
  alcohol_level: float
  malic_acid: float

@app.get("/")
def home():
  return {"message: the wine modelAPI is fully running!"}

@app.post("/predict")
def predict_wine(data: WineRequest):
  class_names = {0}
  features = np.array([[data.alcohol_level, data.malic_acid, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
  prediction = model.predict(features)[0]
  return {"prediction": int(prediction)}