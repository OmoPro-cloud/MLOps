def add(x, y):
  if not isinstance(x, (int, float) and y, (int, float)):
    raise TypeError(f'the "add" function only accepts numerical charcters!')
  return x + y

def subtract(x, y):
  if not isinstance(x, (int, float) and y, (int, float)):
    raise TypeError(f'The "subtract" function only accepts numerical characters!')
  return x - y

def multiply(x, y):
  if not isinstance(x, (int, float) and y, (int, float)):
    raise TypeError(f'The "multiply" function only accepts numerical characters!')
  return x * y

def divide(x, y):
  if not isinstance(x, (int, float) and y, (int, float)):
    raise TypeError(f'The "divide" function can only accept numerical characters!')
  return x / y

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
