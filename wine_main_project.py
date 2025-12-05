from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import os

app = FastAPI()

# Load model at startup
model = joblib.load("wine_model.pkl")

#set path for file so we don't run into "FileNotFoundError: [Errno 2] No such file or directory: 'wine_model.pkl'"
BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "wine_model.pkl")
model = joblib.load(model_path)

class WineRequest(BaseModel):
    alcohol: float
    malic_acid: float
    ash: float

@app.get("/")
def home():
    return {"message: the wine api classifier is running smoothly!"}

@app.post("/predict")
def predict_wine(req: WineRequest):
    x = np.array([[req.alcohol, req.malic_acid, req.ash]])
    pred = model.predict(x)[0]
    mapping = {0: "Cultivar A", 1: "Cultivar B", 2: "Cultivar C"}
    return {"prediction_id": int(pred), "cultivar": mapping.get(int(pred), "Unknown")}