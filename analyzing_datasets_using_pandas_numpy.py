#kaggle.com, huggingface.co and ourworldindata.org are great resources that can be used to analyze datasets
'''
Download a COVID-19 dataset from Kaggle or ourworldindata.org.

Load with Pandas.

Use filtering to show top 10 countries by total cases.

Use groupby to see cases per continent.

Use NumPy to calculate percentage changes over time.
'''

import pandas as pd
import numpy as np


covid_df = pd.read_csv('covid_19.csv')

#top cases
latest_data = covid_df.groupby('country')['total_cases'].max().reset_index()
top10_cases = latest_data.sort_values('total_cases', ascending=False).head(10)
print('Top 10 countries by local cases:')
print(top10_cases)

#use groupby to see cases per continent
total_death_by_country = covid_df.groupby('country')['total_deaths'].max().reset_index()
print('\nTotal deaths by country:')
print(total_death_by_country)