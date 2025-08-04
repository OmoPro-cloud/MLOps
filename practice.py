student ={
  'Name' : 'Jason',
  'Matric_no' : 12,
  'Department' : 'Civil Engineering',
  'GPA' : 4.1
}
print(student)

student['email'] = 'jason@example.com'
print(student)

student['GPA'] = 3.3
print(student)

if student['name'] in student :
  print(student['name'].upper())
print(student['name'])