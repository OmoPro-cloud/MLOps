#Object Oriented Programming in Python
#methods

#class Person:
#  def greet(self):
#    print('Hello, I am a person.')

#Instantiate

#person = Person()
#call method

#person.greet()

#*Modified greeting method
class Person:
  def greet(self, name):
    self.name = name
    print(f'Hello, I am {name}')

person = Person()

person.greet("John")
print(person.name)

class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def bark(self):
    return f'{self.name} says Woof!'
  
  def get_age(self):
    return f'{self.name} is {self.age} years old.'
  
  def walk(self):
    raise NotImplementedError('Subclass has not been implemented')
  
#Usage example

my_dog = Dog('Buddy', 5)
print(my_dog.bark()) #output will be bark
print(my_dog.get_age()) #output will be age
print(my_dog.walk()) #will raise NotImplementedError