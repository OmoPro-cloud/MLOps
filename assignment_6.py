#Write functions for add, subtract, multiply with error checks.
#Create a CLI prompt using input() to perform arithmetic.
#Your code should keep running until the user type "bye"

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  if b == 0:
    print('Error: Cannot divide by zero!')
    return
  print('Division: ', a / b)
  
print('Welcome to the calculator app!')

try:
  num1 = int(input('Enter your first number: '))
  num2 = int(input('Enter your second number: '))
except ValueError:
  print('Error: Please enter valid numbers only')

print('Addition: ', add(num1, num2))
print('Multiplication', multiply(num1, num2))
print('Subtraction: ', (num1, num2))

try:
  print('Division: ', divide(num1, num2))
except ValueError as e:
  print('Error:   Divide: ', e)