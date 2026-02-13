#this file will be used as the authentication 
from fastapi import Header, HTTPException

API_KEYS = [
    "student-key-123",
    "admin-key-456"
]

def verify_api_key(x_api_key: str = Header(..., alias="X-API-Key")):
    if x_api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API Key")