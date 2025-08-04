#Error Handling, functions, for and while loops

while True:
  try:
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))

    result = num1 / num2
    print("Result: ", result)

    if(result % 2 == 0):
      print('The result is even.')
    else:
      print('The result is odd')

    #for loop
    for i in range(5):
      print('Loop iteration: ', i)
  
    #while loop
    count = 0
    while count > 5:
      print('Count: ', count)
      count += 1

  except ValueError:
    print('Error: Please provide valid errors.')
  except ZeroDivisionError:
    print('Error: Division by Zero is not allowed.')
  except Exception as e: #generic
    print('Error: ', e)

#Function
#in python, to create a function, you use def
#functions are usually named after the function it is going to perform

def greet(name):
  print('Hello ' + name + '!')

print('John')

def divide(x, y):
  #Divides x by y and returns the result
  if y == 0:
    raise ValueError('Cannot divide by zero')
  return x / y
def multiply(x, y):
  #multiplies x by y and returns the result
  return x * y
def add(x, y):
  #adds x and y and returns the result
  return x + y

while True:
  print(divide())