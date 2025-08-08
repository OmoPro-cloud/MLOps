def add(x, y):
  if not (isinstance(x, (int, float)) and (isinstance(y, (int, float)))):
    raise TypeError('Error - function requires a numerical input')
  return x + y

def subtract(x, y):
  if not (isinstance(x, (int, float)) and (isinstance(y, (int, float)))):
    raise TypeError('Error - function requires a numerical input')
  return x - y

def multiply(x, y):
  if not (isinstance(x, (int, float)) and (isinstance(y, (int, float)))):
    raise TypeError('Error - function requires a numerical input')
  return x * y

def divide(x, y):
  if not (isinstance(x, (int, float)) and (isinstance(y, (int, float)))):
    raise TypeError('Error - function requires a numerical input')
  return x / y

print('Welcome')

while True:
  op = input('Please select a function: add, subtract, multiply or divide. Press "bye" to exit')

  if op == 'bye':
    print('Farewell')
    break

  if op not in {'add', 'subtract', 'multiply', 'divide'}:
    print('Unknown command - type add, subtract, or multiply.')
    continue

  try:
    x = int(input('Please enter your first number: '))
    y = int(input('Please enter your second number: '))

  except ValueError:
    print('Please enter numerical data for the function!')
    continue

  try:
    if op == 'add':
      result = add(x, y)
    elif op == 'subtract':
      result = subtract(x, y)
    elif op == 'multiply':
      result = multiply(x, y)
    elif op == 'divide':
      result = divide(x, y)
    
  except ValueError as err:
    print('Error - ', err)
    continue

  print('Result = ', result)