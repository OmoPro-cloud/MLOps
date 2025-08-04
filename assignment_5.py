#Write a Python program that:

#Defines a function called factorial(n) that:

#Uses a loop (either for or while) to calculate the factorial of a number.

#Returns the result.

#Ask the user to enter a number.

#Call the factorial function with the user’s number.

#Print the result as:
#"The factorial of [number] is [result]"

def factorial(n):
  result = 1
  for i in range(1, n+1):
    result *= i
  return i


value = int(input('Enter a number: '))
try:
  num = int(value)
except ValueError:
  print('Please provide a valid integer.')
  return
if value < 0:
  print('Factorials can not be defined using negative numbers.')
  return
  
x = factorial(num)

print(f'The factorial of {value} is {x}')