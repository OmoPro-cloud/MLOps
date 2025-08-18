'''
"mathematical-plotting-library"
matplotlib is used 

'''

import matplotlib.pyplot as plt
import pandas as pd

#fig, ax = plt.subplots()
#ax.plot([1, 2, 3], [1, 4, 9], marker='o')
#ax.set(title='Demo Plot', xlabel='X-axis', ylabel='Y-axis')
#plt.show()

#Load csv
df = pd.read_csv('time_series_demo.csv')

#inspect data
print(df.head(10))

#plot the graph
fig, ax = plt.subplots(figsize=(8, 4))
df.plot(df['Year'], df['Value'], marker='o', linewidth=2)
ax.set(title='Time Series Demo', xlabel='Year', ylabel='Value')
ax.grid(True, alpha=0.3)
plt.show()