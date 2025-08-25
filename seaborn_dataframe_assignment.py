import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

df = pd.read_csv('time_series_demo.csv')

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Year', y='Value', hue='Region', marker='o')
plt.title('Value Trends by Region')