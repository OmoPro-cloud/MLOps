import random

def recommend(user_id: int):
    premium = ["iphone", "macbook", "airpods"]
    budget = ["android", "chromebook", "earbuds"]

    if user_id % 2 == 0:
        return random.choice(premium)
    return random.choice(budget)