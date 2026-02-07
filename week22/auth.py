from fastapi import Header, HTTPException
from my_secrets import API_KEYS

def verify_api_key(x_api_key: str = Header(...)):
  if x_api_key not in API_KEYS:
    raise HTTPException(status_code=401, detail="Invalid API Key")
  
from fastapi import FastAPI
from auth import verify_api_key
from fastapi import Depends

app = FastAPI()

@app.get("/predict")
def predict(data: dict, api_key = Depends(verify_api_key)):
  #Your prediction logic here
  return{"prediction": "approved"}
