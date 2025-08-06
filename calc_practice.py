#add functions for add, subtract, divide, multiply

def add(a, b):
  if not isinstance(a, (int, float) and b, (int, float)):
    raise TypeError('the addition function requires numeric types')
  return a + b

def subtract(a, b):
  if not isinstance(a, (int, float) and b, (int, float)):
    raise TypeError('the subtract function requires numeric types')
  return a - b

def divide(a, b):
  if not isinstance(a, (int, float) and b, (int, float)):
    raise TypeError('the divide function requires numeric types')
  return a / b

def multiply(a, b):
  if not isinstance(a, (int, float) and b, (int, float)):
    raise TypeError('the multiplication function requires numeric types')
  return a * b


#calculator(main) interaction

def main():
  print('The Calculator App welcomes you. Type "bye" to exit')

  while True:
    start = input('Select whether you want to add, subtract, divide or multiply')

    if start == "bye":
      print('Farewell.')
      break

    if start not in {"add", "subtract", "divide", "multiply"}:
      print('Unrecognized command - please type add, subtract, multiply or divide')
      continue
