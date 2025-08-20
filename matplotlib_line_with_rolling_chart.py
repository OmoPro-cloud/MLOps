'''
Task 1 – Line Chart with Rolling Mean

Load the CSV into a Pandas DataFrame.

Create a line chart of Year vs Value.

Add a 5-year rolling mean line (dashed).

Add a horizontal line at the mean value.

Annotate the highest peak with an arrow.

Save the figure as line_with_roll.png.

'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('time_series_demo.csv')
print(df)

df['5_Year_Rolling_Mean'] = df['Value'].rolling(window=5).mean()
mean_value = df['Value'].mean()

peak = df['Value'].idxmax()
x_max = df.loc[peak, 'Year']
y_max = df.loc[peak, 'Value']

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df['Year'], df['Value'], marker='o', linewidth=1, label='Value')
ax.plot(df['Year'], df['5_Year_Rolling_Mean'], linestyle='--', linewidth=2, label='5 Year Rolling Mean')
ax.axhline(mean_value, color='k', linestyle=':', linewidth=1.5, label=f'Mean')

ax.annotate(
  f'Max: {y_max:.2f} in {int(x_max)}',
  xy = (x_max, y_max),
  xytext = (x_max, y_max + 0.3),
  arrowprops = dict(facecolor = 'black', arrowstyle='->'),
  ha = 'center'
)

ax.set_title('Time Series with 5 Year Rolling Mean and Peak')
ax.set_xlabel('Year')
ax.set_ylabel('Value')
ax.grid(True, alpha=0.5)
ax.legend()

fig.savefig('line_with_roll.png', dpi=300)
plt.show()

'''
fig, ax = plt.subplots()
ax.plot(df['Year'], df['Value'], marker='o', linewidth=0.5)
ax.set(title='time series demo', xlabel = 'Year', ylabel = 'Value')
ax.grid(True, alpha = 0.5)
plt.show()
'''

