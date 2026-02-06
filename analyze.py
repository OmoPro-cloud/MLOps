import pandas as pd

df = pd.read_csv("metrics.csv", header=None)
df.columns = ["user_id", "model", "item", "latency"]

print(df.groupby("model").agg({
  "latency": "mean",
  "item": "count"
}))