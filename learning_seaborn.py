import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#load data

df = pd.read_csv('time_series_demo.csv')


#convert to df_temp
df_temp = df.rename(columns={'Value': 'temp_anomaly', 'Region':'region'})
df_temp['date'] = pd.to_datetime(df_temp['Year'], format='%Y')
df_temp['year'] = df_temp['date'].dt.year
df_temp['month'] = df_temp['date'].dt.month

#df_temp = 
sns.set_theme(style='whitegrid', context='talk')

#core plot
sns.lineplot(data=df_temp, x='year', y='temp_anomaly')
plt.title('Global temperature anomaly ')
plt.show()

#distribution
sns.histplot(data=df_temp, x='temp_anomaly', bins=10, kde=True)
plt.title('Distribution of gloabal temperature anomalies')
plt.show()