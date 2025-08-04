#virtual environment
#pip install virtualenv
# Install virtualenv (if not installed)
#pip install virtualenv

# Create a virtual environment
#virtualenv venv

# Activate the environment
# Windows
#venv\Scripts\activate
# Mac/Linux
#source venv/bin/activate
print("hello_world")

#Variables and DataTypes
#variables are like a container that holds a specific value
#Data Types are the different types of values that can be stored in a variable
name = "John" #String
age = 30 #Integer
height = 5.9 #Float
is_student = True #Boolean

#simple arithmetic - hard coding
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
#Addition
sum = num1 + num2
print("Sum = ", sum)
#subtraction
difference = num1 - num2
print("Difference = ", difference)
#multiplication
multiplication = num1 * num2
print("Multiplication =", multiplication)
#division
division = num1 / num2
print("Division = ", division)
#modulos
modulos = num1 % num2
print("Modulos = ", modulos)