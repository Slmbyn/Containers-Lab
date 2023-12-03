# Exercise 1
students = ['Selam', 'Will', 'Leah', 'Nathan']
print(students[1])
print(students[-1])


# Exercise 2
foods = ('Pizza', 'Burger', 'Ribs', 'Tacos')

for food in foods:
    print(f'{food} is a good food')

# Exercise 3

for food in foods[2:]:
    print(food)

# Exercise 4

home_town = {
    'city': 'Oakland',
    'state': 'California',
    'population': 450000
}
print(f'I was born in {home_town["city"]}, {home_town["state"]} - population of {home_town["population"]}')

# Exercise 5

for key, value in home_town.items():
    print(f'{key} = {value}')


# Exercise 6

cohort = []

for index, student in enumerate(students):
    cohort.append({
        'student': student,
        'fav_food': foods[index]
    })
print(cohort)


# Exercise 7
# awesome_students = []
# for student in students:
#     awesome_students.append([f"{student} is awesome!"])

# for student in awesome_students:
#     print(student)

awesome_students = [f"{student} is awesome!" for student in students]

for student in awesome_students:
    print(student)

# Exercise 8
a_foods = [food for food in foods if 'a' in food]

for food in a_foods:
    print(food)
