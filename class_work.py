#Write a program that:

#Asks the user to input their name and age.

#Greets the user by name.

#Uses an if statement to check if the user is an adult (age > 18).

#If adult, print "You are an adult."

#Else, print "You are a minor."

#Use a while loop to print "Still young" until the user's age reaches 25.

#📌 Hint: You may increase the age by 1 in each loop until it reaches 25.

print('Welcome to the user database')
name = input('Please enter your name: ')
age = int(input('Please enter your age: '))
print(age)

def greet(name):
  print('Hello, ' + name + ', welcome to the database!')
greet(name)

if age < 18 :
  print('You are a minor')
else:
  print('You are an adult')

while age < 18 :
  print('Still young')
  age += 1
  print(age)
  if age == 25 :
    print('You are now 25!')
