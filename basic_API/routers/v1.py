#this version of the router will use A/B Testing
from fastapi import APIRouter, Depends
from auth import verify_api_key
import random
import time
import csv

from models.model_v1 import recommend as model_a
from models.model_v2 import recommend as model_b

router = APIRouter(prefix="/api/v1", tags=["Version 1"])

TRAFFIC_SPLIT = {
    "A": 0.5,
    "B": 0.5
}

def choose_model():
    return "A" if random.random() < TRAFFIC_SPLIT["A"] else "B"

@router.get("/recommend/{user_id}")
def recommend(user_id: int, api_key=Depends(verify_api_key)):
    model = choose_model()
    start_time = time.time()

    if model == "A":
        item = model_a(user_id)
    else:
        item = model_b(user_id)

    latency = time.time() - start_time

    # log metrics
    with open("metrics.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([user_id, model, item, latency])

    return {
        "version": "v1",
        "user_id": user_id,
        "recommendation": item,
        "model_used": model,
        "latency": latency
    }
