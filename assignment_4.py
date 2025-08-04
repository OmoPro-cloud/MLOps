#Create a function called check_even_odd(number) that:

#Takes a number as input.

#Returns "Even" if the number is even, otherwise returns "Odd".

#Save this function inside a file named helpers.py.

#In another file named main.py:

#Ask the user to enter a number.

#Import the check_even_odd function from helpers.py.

#Print whether the number is even or odd using the function.

def check_even_odd(number):
  if(number % 2 == 0):
    return 'Even'
  else:
    return 'Odd'

