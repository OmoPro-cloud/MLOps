#Data Structures in Python

#list
numbers = [1, 2, 3]
print(numbers)
print(numbers[0])
print(numbers[2])

#Adding an element to the list
numbers.append(50)
print(numbers)

#Removing an element from the list
numbers.remove(2)
print(numbers)

#Looping
for number in numbers:
  print("number: ", number)

#Dictionary

person ={
  'name': 'Jason',
  'age': 30,
  'height': 5.9,
  'is_Student': True,
}

print("Name: ", person['name'])

#add new key
person['email'] = 'jason@example.com'
#Update a key
person['age'] = 31
print("Updated Age: ", person['age'])

#Tuple - immutable sequence
coordinates = (10.0, 20.0)

#Set - unordered collection of unique elements
unique_numbers = [1, 2, 3, 4, 5]

fruits = ['apple', 'pear', 'banana', 'cherry', 'grape']

print(fruits)
fruits.append('tomato')
fruits.append('strawberry')

print(fruits)

fruits.remove('apple')
print(fruits)

for fruit in fruits :
  print(fruit.upper())

#Create a dictionary of a book with title, author, year.

#Add a new key: “price”.

#Change the year to current year.

#Loop and print all key-value pairs.

book = {
  'title' : 'Python Adventures',
  'author' : 'Omoyemi Akomolafe',
  'year' : 2023,
}

print(book)

book.update({'price': 55})

book.update({"year": 2025})
print(book)

#for key, value in student.items():
#    print(f"{key} -> {value}")

for title in book.items():
  print(f"{title} -> {value}")
