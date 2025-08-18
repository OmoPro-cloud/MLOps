import pandas as pd
import numpy as np

e_df = pd.read_csv('ebola.csv', parse_dates=['Date'])

#list countries in order of top 10 cases
latest_cases = e_df.groupby('Country')['Cases'].max().reset_index()
top10_cases = latest_cases.sort_values('Cases', ascending=False).head(10)
print('\nList of Top 10 countries with cases:')
print(top10_cases)


#list of countries in order of top 5 deaths
latest_deaths = e_df.groupby('Country')['Deaths'].max().reset_index()
top10_deaths = latest_deaths.sort_values('Deaths', ascending=False).head(10)
print('\nList of Top 10 countries with deaths:')
print(top10_deaths)


#average amount of cases in all countries
avg_cases = e_df['Cases'].mean()
avg_cases_rounded = round(avg_cases, 2)
print('\nAverage number of cases per country: ', avg_cases_rounded)


#average number of deaths in all countries
avg_deaths = e_df['Deaths'].mean()
avg_deaths_rounded = round(avg_deaths, 2)
print('\nAverage mumber of deaths per country: ', avg_deaths_rounded)



#use groupby to see cases per country
cases_per_country = e_df.groupby('Country')['Cases'].max().reset_index()
print('\nTotal number of cases per country:')
print(cases_per_country)



#use groupby to see deaths per country
deaths_per_country = e_df.groupby('Country')['Deaths'].max().reset_index()
print('\nTotal number of deaths per country:')
print(deaths_per_country)



#use numpy to calculate percentage changes over time
country = 'Germany'

country_df = (
  e_df[e_df['Country'] == country]
  .sort_values('Date')
  .copy()
)

country_df['Percent_Change_In_Cases'] = (
  country_df['Cases']
  .pct_change()
  .mul(100)
)

country_df['Percent_Change_In_Cases'] = country_df['Percent_Change_In_Cases'].round(2)
print('\nPercent Change in Cases in: ', country)
print(country_df[['Date', 'Cases', 'Percent_Change_In_Cases']])





