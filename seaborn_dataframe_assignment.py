import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

df = pd.read_csv('time_series_demo.csv')

#Value Trends by region(lineplot)
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Year', y='Value', hue='Region', marker='o')
plt.title('Value Trends by Region')
plt.xlabel('Year')
plt.ylabel('Value')
plt.legend(title='Region')
plt.tight_layout()
plt.show()

#Average Value per region(barplot)
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x='Year', y='Value', estimator='mean', ci='None', palette='muted')
plt.title('Average Value Per Region')
plt.xlabel('Region')
plt.ylabel('Average Value')
plt.tight_layout()
plt.show()

#Distribution of values by region(boxplot)
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Year', y='Value', palette='pastel')
plt.title('Distribution of values by Region')
plt.xlabel('Region')
plt.ylabel('Value Distribution')
plt.tight_layout()
plt.show()