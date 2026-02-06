import pandas as pd

df = pd.read_csv("metrics.csv", header=None)
df.columns = ["user_id", "model", "item", "latency"]

summary = df.groupby("model").agg({
    "latency": "mean",
    "item": "count"
})

print("Model performance summary:")
print(summary)

winner = summary["latency"].idxmin()
print(f"\nWinning model based on latency: Model {winner}")

#this code will decide the winner based on whoever has the lower latency