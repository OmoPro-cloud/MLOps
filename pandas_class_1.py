import pandas as pd

#PANDAS CLASS

df = pd.read_csv('data.csv') #Assuming data.csv is in the same directory
print(df.head()) #Display the first few rows of the DataFrame

data = {
  'Name': ['Alice', 'Bob', 'Charlie'],
  'Age': [25, 30, 35],
  'City': ['New York', 'Los Angeles', 'Chicago']
}

df1 = pd.DataFrame(data)
print(df1.shape) #displays the shape of the DataFrame
print(df1.columns) #Displays the column names

#Filtering Data
#print people whose age is higher than 25
print(df1[df1['Age'] > 25]) #Filters through rows where age is greater than 25

#people whose age is greater than 25 and live in new york
print(df1[(df1['Age'] > 25) & (df1['City'] == 'Chicago')])

#Grouping and Aggregating Data
#Basic group and mean
df1.groupby('City')['Age'].mean() #will group by city and calculate the mean age of the city

#multiple aggregation
df1.groupby('City').agg({'Age': 'mean', 'Name': 'count'})

covid = pd.read_csv('data.csv')
covid_data_sum = covid.groupby('Country')[['Cases', 'Deaths']].sum()
print(covid_data_sum)

#Get countries with more than 2000 countries
print(covid_data_sum[covid_data_sum['Cases'] > 2000])