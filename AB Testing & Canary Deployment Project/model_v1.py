import random

def recommend(user_id: int):
    # basic popularity model
    items = ["phone", "laptop", "tablet", "headphones"]
    return random.choice(items)