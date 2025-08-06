#add functions for add, subtract, divide, multiply

def add(a, b):
  if not isinstance(a, (int, float) and b, (int, float)):
    raise TypeError('the addition function requires a numerical input')
  return a + b

def subtract(a, b):
  if not isinstance(a, (int, float) and b, (int, float)):
    raise TypeError('the substraction function requires a numerical input')
  return a - b

def multiply(a, b):
  if not isinstance(a, (int, float) and b(int, float)):
    raise TypeError('the multiplication function requires a numerical input')
  return a * b

def divide(a, b):
  if not isinstance(a, (int, float) and b, (int, float)):
    raise TypeError('the multiplication function requires a numerical input')
  return a / b

#calculator(main) interaction

def main():
  print('The Calculator App welcomes you')
  print('type "bye" to exit')

  while True:
    op = input('type "add", "subtract", "multiply", or "divide"').strip().lower()
    if op == "bye":
      print('Farewell')
      break

    if op not in {"add", "subtract", "multiply", "divide"}:
      print('unrecognized input - type add, subtract, divide, multiply')
      continue


main()