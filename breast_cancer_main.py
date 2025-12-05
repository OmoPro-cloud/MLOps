import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="The 'breast_cancer_model.pkl' API is succesfully running!")

model = joblib.load('breast_cancer_model.pkl')

class BreastRequest(BaseModel):
  ID: float
  Diagnosis: float
  radius1: float
  texture1: float
  perimeter1: float
  area1: float
  smoothness1: float
  compactness1: float
  concavity1: float
  concave_points1: float
  symmetry1: float
  fractal_dimension1: float
  radius2: float
  texture2: float
  perimeter2: float
  area2: float
  smoothness2: float
  compactness2: float
  concavity2: float
  concave_points2: float
  symmetry2: float
  fractal_dimension2: float
  radius3: float
  texture3: float
  perimeter3: float
  area3: float
  smoothness3: float
  compactness3: float
  concavity3: float
  concave_points3: float
  symmetry3: float
  fractal_dimension3: float

@app.get("/")
def home():
  return {"The 'breast_cancer_model.pkl' API is succesfully running!"}

@app.post("/predict")
def predict_breast(data: BreastRequest):
  class_names = {0: "Good", 1: "Caution", 2: "Rest in tits"}
  features = np.array([[data.ID, data.Diagnosis, data.radius1, data.texture1, data.perimeter1, data.area1, data.smoothness1, data.compactness1, data.concavity1, data.concave_points1, data.symmetry1, data.fractal_dimension1,
                        data.radius2, data.texture2, data.perimeter2, data.area2, data.smoothness2, data.compactness2, data.concavity2, data.concave_points2, data.symmetry2, data.fractal_dimension2,
                        data.radius3, data.texture3, data.perimeter3, data.area3, data.smoothness3, data.compactness3, data.concavity3, data.concave_points3, data.symmetry3, data.fractal_dimension3]])
  prediction = model.predict(features)[0]
  return {"prediction": class_names[int(prediction)]}