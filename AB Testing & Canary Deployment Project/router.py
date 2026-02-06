from fastapi import APIRouter
import random
import time
import csv

from model_v1 import recommend as model_a
from model_v2 import recommend as model_b

recommend_router = APIRouter()

#splitting traffic into 50-50 for A/B testing
TRAFFIC_SPLIT = {
    "A": 0.5,
    "B": 0.1
}

def choose_model():
    return "A" if random.random() < TRAFFIC_SPLIT["A"] else "B"

@recommend_router.get("/recommend/{user_id}")
def recommend(user_id: int):
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
        "user_id": user_id,
        "recommendation": item,
        "model": model,
        "latency": latency
    }