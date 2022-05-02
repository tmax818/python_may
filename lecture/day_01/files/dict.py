

person_list = ["Tyler", 39, True, True]

person_dict = {'name': 'Tyler', 'age': 39}
address = {'street': "123 Main", 'city': 'Santa Clarita', 'state': 'CA', 'zip': 91355}

person_dict['address'] = address

person_dict['age'] = 46



person_dict['hobbies'] = []

person_dict['hobbies'].append('sleeping')
person_dict['hobbies'].append('coding')

# print(person_dict)
# print(person_dict['hobbies'])


students = [
         {'first_name':  'Cesar', 'age' : 24},
         {'first_name' : 'Tim', 'age' : 26},
         {'first_name' : 'Yo Han', 'age' : 21},
         {'first_name' : 'Alden', 'age' : 23},
         {'first_name' : 'Devin', 'age' : 25}
    ]

new_old_students = []
for student in students:
     print(student['age'])
     if student['age'] > 22:
          new_old_students.append(student)

print(new_old_students)