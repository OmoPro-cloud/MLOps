import random

def recommend(user_id: int):
  #basic popularity model
  items = ["phone", "laptop", "tablet", "headphones"]
  return random.choice(items)

#this code will recommend random popular items. it is not complex but it is very fast