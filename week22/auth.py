from fastapi import Header, HTTPException
from my_secrets import API_KEYS

def verify_api_key(x_api_key: str = Header(..., alias="X-API-Key")):
  if x_api_key not in API_KEYS:
    raise HTTPException(status_code=401, detail="Invalid API Key")
  
from fastapi import FastAPI
from auth import verify_api_key
from fastapi import Depends

app = FastAPI()

@app.get("/predict")
def predict(api_key = Depends(verify_api_key)):
  #Your prediction logic here
  return{"prediction": "approved"}

#cmd command: curl.exe -H "X-API-Key: student-key-123" http://127.0.0.1:8000/predict
#Build a basic  API with API key authentication and versioning+