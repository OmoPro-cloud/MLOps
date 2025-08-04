#2. Dictionaries
#1 - Create a dictionary named student with the following keys:
#name
#matric_no
#department
#gpa

#2 - Add a new key: email

#3 - Update the gpa to a new value.

#4 - Print the student's name in uppercase.

#5 - Loop through the dictionary and print each key-value pair in the format ->
#    key: value

#1
student ={
  'name': 'Jason',
  'matric_no': 4,
  'department': 'Civil Engineer',
  'gpa': 3.6
}
print(student)

#2
student['email'] = 'jason@example.com'
print(student)

#3
student['gpa'] = 4.2
print(student)

#4
if student['name'] in student :
  print(student['name'].upper())
print(student['name'])

#5
for title in student :
  print(student.items())