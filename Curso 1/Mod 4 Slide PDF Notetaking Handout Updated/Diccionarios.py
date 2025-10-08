billy = {
    'name': 'Billy',
    'grades': [100,80,67,100,89],
    'attendance': [True, True, True, True, True]
}

sarah = {
    'name': 'Sarah',
    'grades': [0,99,0,100,0],
    'attendance': [True, False, True, False, True]
}

ben = {
    'name': 'Ben',
    'grades': [60,82,71,92,100],
    'attendance': [False, False, False, False, False]
}


ben = {
    'name': 'Ben',
    'grades': [60,82,71,92,100],
    'attendance': [False, False, False, False, False]
}

students = {'1': billy, '2': sarah, '3': ben}

#Get numbers of students
print(len(students))

#Get all students ids
print(students.keys())

#iterative over students
for k in students:
    print('key', k)

#Get 'billy' attendance
billy = students['1']
print(billy['attendance'])

#Get sarah's grades
sarah = students.get('2')
print(sarah['grades'])

#Get all key:value pairs for be
ben = students.get('3')
items = ben.items()
for key, values in items:
    print(key, values)

#Get average students grade for all asigments
grades = []
items = students.items()
for key, val in items:
    for g in val['grades']:
        grades.append(g)

#grades average
print(round(sum(grades)/len(grades)))

#another way to do this
grades_concatenated = []
items = students.items()

for key, val in items:
    grades_concatenated += val['grades']

#average grade
print(round(sum(grades_concatenated)/len(grades_concatenated)))
