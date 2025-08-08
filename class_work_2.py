#create a new file
#build a simple calculator that can do add, sub, mult

def add(x, y):
  if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
    raise TypeError('This function can only accept numerical values')
  return x + y

def subtract(x, y):
  if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
    raise TypeError('This function can only accept numerical values')
  return x - y

def multiply(x, y):
  if not (isinstance(x, (int, float)) and (isinstance(y, (int, float)))):
    raise TypeError('This function can only accept numerical values')
  return x * y

print('Welcome to the calculator app')

op = input('Please choose whether you would like to add, subtract or multiply')
if op == 'add':
  x = int(input('Please enter your first number: '))
  y = int(input('Please enter your second number: '))
  print(add(x, y))

if op == 'subtract':
  x = int(input('Please add your first number: '))
  y = int(input('Please enter your second number: '))
  print(subtract(x, y))

if op == 'multiply':
  x = int(input('Please enter your first number: '))
  y = int(input('Please enter your second number: '))
  print(multiply(x, y))

print(1)