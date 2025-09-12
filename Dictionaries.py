student = {'name': 'John', 'age': 25, 'course': ['Math','Compsci']}

print(student['name'])
print(student['age'])
print(student['course'])
#it will return an error if the key does not exist

print(student.get('name'))
print(student.get('age'))
print(student.get('course'))
print(student.get('phone'))
#it will return None if the key doesnt exist

student.update({'name': 'Ceejay', 'age' : 20, 'phone': '555-55'})
#to update the student dictionary

print(student.get('name'))
print(student.get('age'))
print(student.get('course'))
print(student.get('phone'))

age = student.pop('age')
#this will remove the age from the dictionary then store it in the age variable

print(age)
print(student)

print(student.keys()) #to get all the keys in the dict
print(student.values()) #to get all the values in the dict

#to loop dicts
for key, value in student.items():
    print(key, value)
    
