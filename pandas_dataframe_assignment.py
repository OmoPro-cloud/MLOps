'''
Homework:

create a csv with your own sales data(date, product, price, quantity)
load it into pandas
Find:
the most expensive product sold
total quantity sold for each product
the day with the highest sales revenue

'''
import pandas as pd

df = pd.read_csv('sales.csv') #load it into pandas
print(df)

print(df[df['Prices'] > 50.00]) #the most expensive product sold

result = df.groupby('Product')['Quantity'].sum() 
print(result) #total quantity sold for each product

#day with the highest sales revenue

df['Revenue'] = df['Prices'] * df['Quantity'] #create a new revenue column

df['Date'] = pd.to_datetime(df['Date']) #convert date column to actual dates

daily_revenue = df.groupby('Date')['Revenue'].sum() #group by date and sum up the revenue for each day

max_rev_date = daily_revenue.idxmax() #finding the date with the highest total revenue
max_revenue = daily_revenue.max()

print(f'The day which recorded the highest sales revenue was {max_rev_date}, \n'
      f'with a total revenue of: ${max_revenue:,.2f}.')