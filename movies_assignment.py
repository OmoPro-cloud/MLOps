import pandas as pd

'''
Find and print:

The movie with the highest rating.

The average rating for each genre.

The number of movies released after the year 2010.
'''

movies = pd.read_csv('movies.csv')

highest_rating = movies.loc[movies['Rating'].idxmax(), 'Title']
print(highest_rating)

average_rating = movies['Rating'].mean()
print(average_rating)

released = movies[movies['Year'] > 2010].shape[0]
print(released)

