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

#Core Concepts of OOP

#Encapsulation - keeps data safe and organized

class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def bark(self):
    return f'{self.name} says Woof!'
  
  def get_age(self):
    return f'{self.name} is {self.age} years old.' #getter methods: its main function is to get information
  
  def walk(self):
    return f'{self.name} is happily going on a walk.'
  
  def rename(self, new_name): #setter method
    self.name = new_name
    return f'The dog has changed their name to {self.name}'
  
#To make a variable private we use '__'
#This is beneficial because it makes protects data and makes unauthorized access impossible
#Example: self.__name

#Inheritance - will give you features from other classes

class ServiceDog(Dog):
  def guide(self):
    return f'Our service dog is trained to guide and assist visually impaired individuals.'
  
  def sit(self):
    return f'{self.name} is trained to sit.'
  
  def bark(self):
    return f'{self.name} barks softly to alert the owner' #this is an example of polymorphism
  
serviceDog = ServiceDog('Buddy', 3, 'Poodle')
print(serviceDog.bark())
print(serviceDog.sit())

#Polymorphism - allows the same method name to perform different tasks
# the most popular form of polymorphism is overriding methods in subclasses

#Abstraction - hides the internal workings of a class
#abstract classes cannot do anything, they simply service as a blueprint for the other classes

#Abstraction in Python
from abc import ABC, abstractmethod

class Animal(ABC):
  def sound(self):
    pass

class Dog(Animal):
  def sound(self):
    return 'Woof!'
  
class Cat(Animal):
  def sound(self):
    return 'Meow!'
  
class Cow(Animal):
  def sound(self):
    return 'Moo!'
  
#Usage example
def animal_sound(animal: Animal):
  print(animal.sound)

if __name__ == '__main__':
  dog = Dog()
  cat = Cat()
  cow = Cow()

  animal_sound(dog)
  animal_sound(cat)
  animal_sound(cow)