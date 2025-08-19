'''
"mathematical-plotting-library"
data vizualization is the display of information in the form of a diagram, infographics, animations or a chart
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
#fig, ax = plt.subplots(figsize=(8, 4))
#ax.plot(df['Year'], df['Value'], marker='o', linewidth=2, linestyle='--')
#ax.set(title='Time Series Demo', xlabel='Year', ylabel='Value')
#ax.grid(True, alpha=0.3)
#plt.show()

roll = df['Value'].rolling(window=5, min_periods=1).mean()
fig, ax = plt.subplots(figsize=(9, 4))

#Original Line
ax.plot(df['Year'], df['Value'], label='Annual Value', linewidth=2)

#Rolling mean line(rolling mean is a moving average, it calculates a trend over a set of time using a set of data)
ax.plot(df['Year'], roll, label='5 Year Rolling Mean', linewidth=2, linestyle='--')

#Reference line at mean
ax.axhline(df['Value'].mean(), color='k', linewidth=1, alpha=0.5)

#Annotate peak
peak_year = df.loc[df['Year'].idxmax(), 'Year']
peak_value = df['Value'].max()
ax.annotate(f'Peak: {peak_value}', xy={peak_year, peak_value},
            xytext = (peak_year + 1, peak_value + 5),
            arrowprops = dict(facecolor = 'black', shrink = 0.05))

#Styling
ax.legend()
ax.set(title = 'Styling and Annotations', xlabel = 'Year', ylabel='Value')
ax.grid(True, alpha=0.3)
plt.show()

'''
Annotate the minimum point instead of maximum.

Add a vertical line at year 2010.

Change rolling window to 3 or 10.
'''