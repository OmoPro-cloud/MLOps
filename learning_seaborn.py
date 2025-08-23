import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#load data

df = pd.read_csv('time_series_demo.csv')
sns.set_theme(style='whitegrid', content='talk')

#core plot
df_temp = df.rename(columns={'Value': 'temp_anomaly', 'Region':'region'})
df_temp['date'] = pd.to_datetime(df_temp['Year'], format='%Y')
df_temp['year'] = df_temp['date'].dt.year
df_temp['month'] = df_temp['date'].dt.month
#df_temp = 
sns.lineplot(data=df_temp, x='Year', y='Value')