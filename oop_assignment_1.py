class Dog():
  def __init__(self, name, age, breed):
    self.name = name
    self.age = age
    self.breed = breed

  def bark(self):
    return f'{self.name} says Woof!'
  
  def get_age(self):
    return f'{self.name} is {self.age} years old'
  
  def walk(self):
    return f'{self.name} is happily walking.'
  
  def get_breed(self):
    return f'{self.name} is a {self.breed}.'
  
  def celebrate_birthday(self):
    self.age += 1
    return f'{self.name} is now {self.age} years old. Happy Birthday, {self.name}!'
  
  def rename(self, new_name):
    self.name = new_name
    return f'The dog has changed their name to {self.name}'
  
  def compare_age(self, other_dog):
    if self.age > other_dog.age:
      return f'{self.name} is older than {other_dog.age}'
    elif self.age < other_dog.age:
      return f'{other_dog} is older than {self.name}'
    else:
      return f'{self.name} and {other_dog} are the same age.'
  
my_dog = Dog('Jett', 5, 'German Shepherd')
print(my_dog.bark())
print(my_dog.get_age())
print(my_dog.walk())
print(my_dog.get_breed())
print(my_dog.celebrate_birthday())
print(my_dog.rename('Jill'))

dog1 = Dog('Buddy', 3, 'Golden Retriever')
dog2 = Dog('Luna', 5, 'Beagle')
dog3 = Dog('Max', 2, 'Pitbull')

print(dog1.bark())
print(dog2.bark())
print(dog3.bark())

print(dog1.get_age())
print(dog2.get_age())
print(dog3.get_age())

print(dog1.get_breed())
print(dog2.get_breed())
print(dog3.get_breed())

print(dog1.celebrate_birthday())

print(dog1.rename('Luther'))

print(dog1.walk())
print(dog2.walk())
print(dog3.walk())

print(dog1.compare_age(my_dog))