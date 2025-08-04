#Assignment 1: Personal Profile Program
#Task:
#Write a Python program that stores your personal details using variables and prints them out in a formatted way.

#Requirements:

#Use at least one variable each for: name (string), age (integer), height (float), and whether you're a student (boolean).

#Print the details clearly like this:


#Name: John 
#Age: 20  
#Height: 5.8  
#Is Student: True  

print("Personal Profile Program")
print("Please input all relevant data")
name = input("Please enter your full name: ")
age = int(input("Please enter your age: "))
height = input("Please enter your height: ")
isStudent = input("Are you currently a student? ")
print("Thank you for providing all the necessary data!")

print("Name: ", name)
print("Age: ", age)
print("Height: ", height)
print("Currently a student? ", isStudent)