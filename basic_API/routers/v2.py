#version 2 of the router will remove the A/B testing and only use the improved version
from fastapi import APIRouter, Depends
from auth import verify_api_key
import time
from models.model_v2 import recommend as model_v2

router = APIRouter(prefix="/api/v2", tags=["Version 2"])

@router.get("/recommend/{user_id}")
def recommend(user_id: int, api_key=Depends(verify_api_key)):
    start_time = time.time()

    item = model_v2(user_id)

    latency = time.time() - start_time

    return {
        "version": "v2",
        "user_id": user_id,
        "recommendation": item,
        "model_used": "model_v2",
        "latency": latency
    }