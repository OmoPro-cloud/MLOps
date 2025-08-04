#1. Lists
#Create a list called cities containing 5 city names.

#2 - Add 2 more cities to the list.

#3 - Remove one city from the list.

#4 - Print all the cities in title case using a loop (e.g., Abuja, not abuja).

#5 - Print the total number of cities in the list.

#1
cities = ['tokyo', 'nagasaki', 'soweto', 'durban', 'lagos']
print(cities)

#2
cities.append('london')
cities.append('berkley')
print(cities)

#3
cities.remove('london')
print(cities)

#4
for letter in cities :
  print(letter.upper())
print(letter)

#5
total_cities = len(cities)
print(f'The list has ', total_cities, ' cities')