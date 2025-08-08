def add(a, b):
  if not (isinstance(a, (int, float)) and (isinstance(b, (int, float)))):
    raise TypeError('Error - function requires a numerical input')
  return a + b

def subtract(a, b):
  if not (isinstance(a, (int, float)) and (isinstance(b, (int, float)))):
    raise TypeError('Error - function requires a numerical input')
  return a - b

def multiply(a, b):
  if not (isinstance(a, (int, float)) and (isinstance(b, (int, float)))):
    raise TypeError('Error - function requires a numerical input')
  return a * b

def divide(a, b):
  if not (isinstance(a, (int, float)) and (isinstance(b, (int, float)))):
    raise TypeError('Error - function requires a numerical input')
  return a / b

while True:
  print('Welcome')
  op = input('Please select a function: add, subtract, multiply, or divide. Type "bye" to exit the application: ').strip().lower()
  print(op)

  if op == 'bye': 
    print('Farewell')
    break

  if op not in {'add', 'subtract', 'divide', 'multiply'}:
    print('Unrecognized request. Enter a valid function.')
    continue

  try:
    a = int(input('Enter your first number: '))
    b = int(input('Enter your second number: '))
  except ValueError:
    print('Error - invalid input')
    continue
    
  print(a, b)
  
  if op == 'add':
    result = add(a, b)
  elif op == 'subtract':
    result = subtract(a, b)
  elif op == 'multiply':
    result = multiply(a, b)
  elif op == 'divide':
    result =  divide(a, b)
  
  print('Result: ', result)
