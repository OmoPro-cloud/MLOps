#Assignment – Extended Dog Class
#Modify the Dog class to include the following:

#An additional attribute called breed. X

#A method called celebrate_birthday() that increases the dog's age by 1 and returns a message like:
#"Buddy is now 6 years old. Happy Birthday!" X

#Update the walk() method so it returns a message like:
#"Buddy is walking happily in the park." X

#Add a method rename(new_name) to change the dog's name.

#Create at least 3 dog objects with different names, ages, and breeds.
#Demonstrate usage of all methods in your program:

#Make each dog bark.

#Print their age and breed.

#Make one dog celebrate its birthday.

#Rename one dog.

#Make all dogs walk.

#Bonus Task (Optional):
#Create a method compare_age(other_dog) that compares two dogs' ages and returns a message stating which dog is older.


#Expected Skills Practiced:

#__init__ constructor

#Instance variables

#Writing multiple methods

#Passing objects as parameters (bonus)

class Dog:
  def __init__(self, name, age, breed):
    self.name = name
    self.age = age
    self.breed = breed

  def bark(self):
    return f'{self.name} says Woof!'
  
  def get_age(self):
    return f'{self.name} is {self.age} years old.'
  
  def get_breed(self):
    return f'{self.name} is a {self.breed}!'
  
  def walk(self):
    return f'{self.age} is walking happily in the park.'
  
  def celebrate_birthday(self):
    self.age += 1
    return f'{self.name} is now {self.age} years old. Happy Birthday, {self.name}!'
  
  def rename(self, new_name):
    self.name = new_name
    return f'The dog has changed their name to {new_name}.'
  
  
my_dog = Dog('Jett', 5, 'German Shepherd')
print(my_dog.bark())
print(my_dog.get_age())
print(my_dog.get_breed())
print(my_dog.celebrate_birthday())
print(my_dog.walk())
print(my_dog.rename('Jill'))