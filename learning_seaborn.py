import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

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
sns.histplot(data=df_temp, x='temp_anomaly', bins=10, kde=True)#histplot is used for distribution
plt.title('Distribution of gloabal temperature anomalies')
plt.show()
'''
To Do: a categorical comparison(.boxplot) and heatmap
'''

#Faceting for small multiples
g = sns.relplot(data=df_temp, x='year', y='temp_anomaly', col='region', kind='line', col_wrap=3, height=2.6)
g.figure.suptitle('Regional Trends', y=1.02)
plt.show()

#plotly is interactive
#fig = px.line(df_temp, x='year', y='temp_anomaly', color='region', title='Interactive: Gloabl Temperature Anomalies by Region')
fig = px.histogram(df_temp, x='temp_anomaly', nbins=30, marginal='box', title='Distribution of global temperatue anomalies')
fig.update_layout(legend_title_text='Region')
fig.write_html('temp_anomalies.html')
fig.show()

