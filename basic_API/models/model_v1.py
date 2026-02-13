import random

def recommend(user_id: int):
    items = ["phone", "laptop", "tablet", "headphones"]
    return random.choice(items)